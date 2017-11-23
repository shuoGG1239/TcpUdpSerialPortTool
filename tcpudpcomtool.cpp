#include "tcpudpcomtool.h"


TcpUdpComTool::TcpUdpComTool(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::TcpUdpComTool)
{
    this->ui->setupUi(this);
    this->setWindowTitle("Tcp Udp Com Tool");
    this->setFixedSize(WIN_WIDTH, WIN_HEIGHT);
    myconfig=new ConfigFileshuoGG("condat.ini");//读取配置文件
    this->comboboxInit();
    this->configDataInit();

    ui->pushButtonSend->setEnabled(false);
    ui->pushButtonSend->setShortcut(QKeySequence("Ctrl+Return"));//快捷键,也可以在QtDesign直接填

    this->setFocusPolicy(Qt::ClickFocus);//随便点击便聚焦
}

TcpUdpComTool::~TcpUdpComTool()
{
    this->configDataSave();
    delete myconfig;
    delete ui;
}

/**
 * @brief 配置文件的初始化
 *
 */
void TcpUdpComTool::configDataInit()
{
    //发送状态读取
    if(myconfig->getValueInteger("sendStatus")==DataOperate::CHAR_STYLE)
        ui->radioButtonString->click();
    else
        ui->radioButton16->click();
    //接收状态读取
    if(myconfig->getValueInteger("recStatus")==DataOperate::CHAR_STYLE)
        ui->checkBoxHexRec->setChecked(false);
    else
        ui->checkBoxHexRec->setChecked(true);
    //上次波特率读取
    ui->comboBoxBaud->setCurrentText(myconfig->getValueString("baudValue"));
    //上次com号
    this->oldcomNum=myconfig->getValueString("comNum");
    //ip和port
    ui->lineEditIpAim->setText(myconfig->getValueString("aimIp"));
    ui->lineEditPortLocal->setText(myconfig->getValueString("srcPort"));
    ui->lineEditPortAim->setText(myconfig->getValueString("dstPort"));
}

/**
 * @brief 保存参数到配置文件
 *
 */
void TcpUdpComTool::configDataSave()
{
    myconfig->setValue("sendStatus",getRadioButtStat());
    myconfig->setValue("recStatus",getCheckBoxStat());
    myconfig->setValue("baudValue",ui->comboBoxBaud->currentText());
    myconfig->setValue("srcPort",ui->lineEditPortLocal->text());
    myconfig->setValue("dstPort",ui->lineEditPortAim->text());
    myconfig->setValue("aimIp",ui->lineEditIpAim->text());
    myconfig->setValue("hostIp",ui->comboBoxLocal->currentText());
    if(NULL !=ui->comboComNum->currentText())
        myconfig->setValue("comNum",ui->comboComNum->currentText());
}

/**
 * @brief 各种combobox组合框的初始化
 *
 */
void TcpUdpComTool::comboboxInit()
{
    /*工具选择框combox*/
    ui->comboBoxStyle->insertItem(0,"UDP");
    ui->comboBoxStyle->insertItem(1,"TCP Client");
    ui->comboBoxStyle->insertItem(2,"TCP Server");
    ui->comboBoxStyle->insertItem(3,"COM Tool");
    connectModeList<<"UDP"<<"TCP Client"<<"TCP Server"<<"COM Tool"; //使用这个Stringlist是为了方便用switch,条理清晰
    connect(ui->comboBoxStyle,SIGNAL(activated(const QString &)), this,SLOT(comboxClicked(const QString &)));//某一项被点击
    /*波特率combox*/
    ui->comboBoxBaud->insertItems(0, SerialPort::baudList);
    ui->comboBoxBaud->setCurrentText("9600");
    ui->comboBoxBaud->hide();
    ui->comboComNum->hide();
    ui->comboBoxClientList->hide(); //tcp的server专用的组合框
    /*本地IP combox*/
    myHostInfo=QHostInfo::fromName(QHostInfo::localHostName());//本地信息获取
    QStringList hostIpList;
    QString oldHostIp;
    QString tempHostIp;
    hostIpList = ICommunicateTCPIP::getLocalIpList();
    oldHostIp = myconfig->getValueString("hostIp");
    foreach (QString ip, hostIpList)
    {
        ui->comboBoxLocal->addItem(ip);
        if(oldHostIp == ip)
            tempHostIp = ip;
    }
    ui->comboBoxLocal->setCurrentText(tempHostIp);
    myaddress= ui->comboBoxLocal->currentText();
}

/**
 * @brief 按下"连接"后各tool的行为
 *
 */
void TcpUdpComTool::connectUDP()
{
    udpSocket = new UdpSocket(this);
    udpSocket->createConnection(myaddress,ui->lineEditPortLocal->text().toInt());
    udpSocket->connectRec(this,SLOT(dataReceivedUDP()));
    ui->pushButtonSend->setEnabled(true);
    ui->labelStatus->setText("UDP创建OK");
}
void TcpUdpComTool::connectTCPclient()
{
    bool isConnectOK;
    tcpSocketClient = new TcpSocketClient(this);
    tcpSocketClient->connectRec(this, SLOT(dataReceivedTCP_client()));
    isConnectOK = tcpSocketClient->createConnection(ui->lineEditIpAim->text(),
                                                    ui->lineEditPortAim->text().toInt());
    if(isConnectOK)
    {
        ui->lineEditIpAim->setEnabled(false);
        ui->lineEditPortAim->setEnabled(false);
        ui->labelStatus->setText("TCP客户端创建OK");
    }
    else
    {
        QMessageBox::information(this,"error","连接失败");
        return;
    }
    ui->pushButtonSend->setEnabled(true);
}
void TcpUdpComTool::connectTCPserver()
{
    tcpServer=new TcpServer(this);
    tcpServer->createConnection(ui->comboBoxLocal->currentText(),
                                ui->lineEditPortLocal->text().toInt());
    //有TCPclient连接上server时
    tcpServer->connectClientConnected(this, SLOT(updateClientList(QString)));
    //当server收到client的发来的数据时
    tcpServer->connectClientDisconnected(this, SLOT(disconnectTCPlist(QString)));
    //有TCPclient断开连接时
    tcpServer->connectRec(this, SLOT(dataReceivedTCP_server(QString)));

    ui->lineEditIpAim->setEnabled(false);
    ui->lineEditPortAim->setEnabled(false);
    ui->pushButtonSend->setEnabled(false);
    ui->comboBoxClientList->show();
    ui->labelStatus->setText("TCP服务端创建OK");
}
void TcpUdpComTool::connectCOM()
{
    serialPort = new SerialPort(this);
    serialPort->connectRec(this,SLOT(comReadData()));
    bool isOpenSuccess = serialPort->openPort(ui->comboComNum->currentText(),
                                              ui->comboBoxBaud->currentText().toInt());
    //打开串口
    if(isOpenSuccess)
    {
        ui->labelStatus->setText(serialPort->getCurPortName()+" OK");
        ui->pushButtonStart->setText("断开");
        ui->pushButtonSend->setEnabled(true);
        ui->comboComNum->setEnabled(false);
        ui->comboBoxBaud->setEnabled(false);
    }
    else
        ui->labelStatus->setText(serialPort->getCurPortName()+" Error");
}


/**
 * @brief 获取radioButt的状态:
 *        选择发送16进制or字符串
 *
 * @return DataOperate::HexOrChar
 */
DataOperate::HexOrChar TcpUdpComTool::getRadioButtStat()
{
    if(ui->radioButton16->isChecked())
        return DataOperate::HEX_STYLE;
    if(ui->radioButtonString->isChecked())
        return DataOperate::CHAR_STYLE;
    return DataOperate::CHAR_STYLE; //warning太烦人,象征性
}

/**
 * @brief 获取勾框的状态:
 *        选择接受显示16进制or字符串
 * @return DataOperate::HexOrChar
 */
DataOperate::HexOrChar TcpUdpComTool::getCheckBoxStat()
{
    if(ui->checkBoxHexRec->isChecked())
        return DataOperate::HEX_STYLE;
    else
        return DataOperate::CHAR_STYLE;
}


/**********************************TcpUdpComTool slots**********************************************/
/***************有client从服务器断开****************/
void TcpUdpComTool::disconnectTCPlist(QString fullAddrStr)
{
    int removeIndex = ui->comboBoxClientList->findText(fullAddrStr);//找出文字对应的index
    ui->comboBoxClientList->removeItem(removeIndex);              //根据index移除该项
    if(ui->comboBoxClientList->count() == 0) //client列表为空时,不允许发送
        ui->pushButtonSend->setEnabled(false);
}
/***************有client连上了服务器****************/
void TcpUdpComTool::updateClientList(QString fullAddrStr)
{
    if(ui->comboBoxClientList->count() == 0)
    {
        tcpServer->setCurClient(fullAddrStr);
    }
    ui->comboBoxClientList->addItem(fullAddrStr);
    ui->pushButtonSend->setEnabled(true);
}

/************接收到数据时的slots*************/
void TcpUdpComTool::dataReceivedUDP()
{
    QByteArray data = udpSocket->read();
    this->recByStyle(data);
}
void TcpUdpComTool::dataReceivedTCP_client()
{
    QByteArray data;
    data = tcpSocketClient->read();
    this->recByStyle(data);
}
void TcpUdpComTool::dataReceivedTCP_server(QString recFromFullAddr)
{
    QByteArray data;
    QString uiCurClientFullAddr;
    uiCurClientFullAddr = ui->comboBoxClientList->currentText();
    //tcpServer->setCurClient(uiCurClientFullAddr);
    //过滤掉其他非comboBoxClientList当前Client的接收数据
    if(uiCurClientFullAddr == recFromFullAddr)
    {
        data = tcpServer->read();
        this->recByStyle(data);
    }
}
void TcpUdpComTool::comReadData()
{
    QByteArray data=serialPort->read();
    this->recByStyle(data);
}

/**********************************button slots**********************************************/
/**
 * @brief 开始创建连接
 *
 */
void TcpUdpComTool::on_pushButtonStart_clicked()
{
    /**********************连接************/
    if(ui->pushButtonStart->text()=="连接")
    {
        ui->pushButtonStart->setText("断开");
        ui->comboBoxLocal->setEnabled(false);
        ui->lineEditPortLocal->setEnabled(false);
        ui->comboBoxStyle->setEnabled(false);
        switch (connectModeList.indexOf(ui->comboBoxStyle->currentText()))
        {
        case UDP_MODE:/*UDP连接*/
            connectUDP();
            break;
        case TCP_CLIENT_MODE:/*TCP客户端连接*/
            connectTCPclient();
            break;
        case TCP_SERVER_MODE:/*TCP服务器连接*/
            connectTCPserver();
            break;
        case SERIAL_PORT_MODE:/*串口模式*/
            connectCOM();
            break;
        }
    }
    /*************************断开************/
    else if(ui->pushButtonStart->text()=="断开")
    {
        switch (connectModeList.indexOf(ui->comboBoxStyle->currentText()))
        {
        case UDP_MODE: /*UDP断开*/
        {
            udpSocket->close();
            delete udpSocket;
        }
            break;
        case TCP_CLIENT_MODE:/*TCP client断开*/
        {
            tcpSocketClient->close();
            ui->lineEditIpAim->setEnabled(true);
            ui->lineEditPortAim->setEnabled(true);
            delete tcpSocketClient;
        }
            break;
        case TCP_SERVER_MODE: /*TCP server断开*/
        {
            tcpServer->close();
            ui->comboBoxClientList->clear();
            ui->comboBoxClientList->hide();
            ui->lineEditIpAim->setEnabled(true);
            ui->lineEditPortAim->setEnabled(true);
            delete tcpServer;
        }
            break;
        case SERIAL_PORT_MODE:
        {
            ui->comboComNum->setEnabled(true);
            ui->comboBoxBaud->setEnabled(true);
            serialPort->close();
            delete serialPort;
        }
            break;
        }
        ui->pushButtonSend->setEnabled(false);
        ui->comboBoxLocal->setEnabled(true);
        ui->lineEditPortLocal->setEnabled(true);
        ui->pushButtonStart->setText("连接");
        ui->comboBoxStyle->setEnabled(true);
        ui->labelStatus->setText("未连接");
    }

}

/**
 * @brief 发送数据按钮
 *
 */
void TcpUdpComTool::on_pushButtonSend_clicked()
{
    QString msg = ui->plainTextEditSend->toPlainText();
    QString aimIP = ui->lineEditIpAim->text();
    int aimPort = ui->lineEditPortAim->text().toInt();
    QByteArray tempArray;
    DataOperate::HexOrChar hexORchar = getRadioButtStat();
    if(hexORchar == DataOperate::HEX_STYLE)//16进制形式
    {
        tempArray = DataOperate::hexStringTochars(msg);
    }
    if(hexORchar == DataOperate::CHAR_STYLE)//字符串形式
    {
        tempArray = msg.toLatin1();
    }

    switch (connectModeList.indexOf(ui->comboBoxStyle->currentText()))
    {
    case UDP_MODE: /*UDP发送*/
    {
        udpSocket->send(tempArray, aimIP, aimPort);
    }
        break;
    case TCP_CLIENT_MODE:/*TCP client发送*/
    {
        tcpSocketClient->send(tempArray);
    }
        break;
    case TCP_SERVER_MODE: /*TCP server发送*/
    {
        tcpServer->setCurClient(ui->comboBoxClientList->currentText());
        tcpServer->send(tempArray);
    }
        break;
    case SERIAL_PORT_MODE:
    {
        /*将data发送到指定ip和端口*/
        serialPort->send(tempArray);
    }
        break;
    }
}

/**
 * @brief 清空接收框
 *
 */
void TcpUdpComTool::on_pushButtonClearRec_clicked()
{
    ui->plainTextEditRec->clear();
}
/**
 * @brief 快捷键提示窗口
 *
 */
void TcpUdpComTool::on_toolButtonShortCut_clicked()
{
    DialogHelpShortcut shortCutWindow;
    //    shortCutWindow.setGeometry(this->x()+(this->width()-shortCutWindow.width())*0.5,
    //                               this->y()+(this->height()-shortCutWindow.height())*0.5,
    //                               shortCutWindow.width(),shortCutWindow.height());
    shortCutWindow.exec();
}



/**
 * @brief 当工具选择的combox某一项被点击时的响应事件
 *
 * @param selectedText
 */
void TcpUdpComTool::comboxClicked(const QString &selectedText)
{
    if("COM Tool"==selectedText)
    {
        ui->comboBoxBaud->show();
        ui->comboComNum->show();
        ui->comboComNum->clear();
        /*扫描电脑存在连接的串口com并将其portname加入combox*/
        foreach(QString strport, serialPort->getSerialPortList())
        {
            ui->comboComNum->addItem(strport);
        }
        if( (NULL != oldcomNum) && (-1 != ui->comboComNum->findText(oldcomNum)) )
        {
            ui->comboComNum->setCurrentText(oldcomNum);
        }
        ui->groupBoxLocal->hide();
        ui->groupBoxAim->hide();

    }
    else
    {
        ui->comboBoxBaud->hide();
        ui->comboComNum->hide();
        ui->groupBoxLocal->show();
        ui->groupBoxAim->show();
    }
}

/**
 * @brief 当本地ip combox中的选项被选中时触发
 *
 * @param arg1 被选中并点击的选项的text
 */
void TcpUdpComTool::on_comboBoxLocal_activated(const QString &arg1)
{
    this->myaddress=arg1;
}


/**
 * @brief  给窗口设置快捷键: ctrl+1==清输出框 ctrl+2==清输入框 ctrl+~==全清
 *
 * @param e 此时窗口发生的事件
 */
void TcpUdpComTool::keyPressEvent(QKeyEvent *e)
{
    if ((e->modifiers() ==Qt::ControlModifier)
            && (e->key() == Qt::Key_1))
    {
        ui->plainTextEditRec->clear();
    }
    if ((e->modifiers() ==Qt::ControlModifier)
            && (e->key() == Qt::Key_2))
    {
        ui->plainTextEditSend->clear();
    }
    if ((e->modifiers() ==Qt::ControlModifier)
            && (e->key() == Qt::Key_QuoteLeft))
    {
        ui->plainTextEditRec->clear();
        ui->plainTextEditSend->clear();
    }
}

/*相当于实现了this->setFocusPolicy(Qt::ClickFocus);*/
//void TcpUdpComTool::mousePressEvent(QMouseEvent *e)
//{
//    if(e->button()==Qt::LeftButton)
//    this->setFocus();
//}


/*******************************************inline***************************************************/
/**
 * @brief 内联函数,根据checkbox对字符串进行转换
 *
 * @param bytesData
 */
inline void TcpUdpComTool::recByStyle(QByteArray &bytesData)
{
    if(getCheckBoxStat()==DataOperate::CHAR_STYLE)
        ui->plainTextEditRec->insertPlainText(QString::fromLatin1(bytesData));
    else if(getCheckBoxStat()==DataOperate::HEX_STYLE)
        ui->plainTextEditRec->insertPlainText(DataOperate::charsToHexString(bytesData));
}


