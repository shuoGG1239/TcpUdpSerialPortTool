#include "tcpserver.h"

TcpServer::TcpServer(QObject *parent) :
    QTcpServer(parent)
{
}

TcpServer::~TcpServer()
{
}


/**
 * @brief 有 client连上服务器则触发此函数,系统会自动分配个handle句柄(唯一码)给这个新socket
 *        最后将 新连接的句柄,ip,port的信号发送出去
 *
 *        原理分析:
 *              当有一个client连接到server, 则 server这边也new一个tcpsocket与client进行一对一通信,
 *              我这里命名为serverClient其实不是很妥当, 应该叫serverSocket比较好。所有有n个tcp连接
 *              就会有n对tcpsocket， 一个是客服端的，一个是服务端new出来与其配对的。
 *              这个类里面的curClient指的是应用层上的"当前"的服务端的tcpSocket, 它的socketID就是curClientID;
 *
 * @param handle socket句柄,相当于socket的唯一码,以辨识哪个socket
 */
void TcpServer::incomingConnection(int handle)
{
    TcpSocketClient *serverClient = new TcpSocketClient(this);
    serverClient->setTcpClientID(handle);
    serverClient->setSocketDescriptor(handle); //核心连接句
    serverClient->setPeerFullAddrStr(toFullAddrStr(serverClient->getPeerIp(),serverClient->getPeerPort()));
    serverClient->connectRecWithClientID(this, SLOT(dataReceived(int)));
    serverClient->connectDisconnectWithClientID(this, SLOT(oneClientDisconnected(int)));
    //存储新连接
    this->mapClientId2Client.insert(handle, serverClient);
    this->mapIpFull2Client.insert(serverClient->getPeerFullAddrStr(), serverClient);

    emit sglOneClientConnected(serverClient->getPeerFullAddrStr());
}

/**
 * @brief 将 Ip和port组合成"192.168.1.100:5001"的格式
 *
 * @param ip
 * @param port
 * @return QString
 */
QString TcpServer::toFullAddrStr(const QString &ip, int port)
{
    QString str;
    str = ip + ':' + QString::number(port);
    return str;
}

/**
 * @brief 设置当前serverSocket, 建议send之前都调用一下
 *
 * @param clientIpPortString
 */
void TcpServer::setCurClient(const QString &clientIpPortString)
{
    this->curClient = this->mapIpFull2Client.value(clientIpPortString);
    this->curClientID = this->curClient->getTcpClientID();
}

/**
 * @brief 新建tcpserver连接, 本质是监听某个端口
 *
 * @param localIP
 * @param localPort
 * @return bool
 */
bool TcpServer::createConnection(const QString &localIP, int localPort)
{
    Q_UNUSED(localIP);
    bool isOK;
    isOK = this->listen(QHostAddress::Any,localPort);  //监听连上本port的任何ip
    return isOK;
}

/**
 * @brief 发送函数还有各种重载版本
 *
 */
void TcpServer::send(QByteArray &data)
{
    this->curClient->send(data);
}

void TcpServer::send(const QString &dataStr)
{
    this->curClient->send(dataStr.toLatin1());
}

void TcpServer::send(QByteArray &data, const QString &dstIp, int dstPort)
{
    QString fullIpPort;
    TcpSocketClient *client;
    fullIpPort = TcpServer::toFullAddrStr(dstIp, dstPort);
    client = this->mapIpFull2Client.value(fullIpPort);
    if( NULL != client)
        client->send(data);
}

void TcpServer::send(const QString &dataStr, const QString &dstIp, int dstPort)
{
    QString fullIpPort;
    TcpSocketClient *client;
    fullIpPort = TcpServer::toFullAddrStr(dstIp, dstPort);
    client = this->mapIpFull2Client.value(fullIpPort);
    if( NULL != client)
        client->send(dataStr.toLatin1());
}

/**
 * @brief 简化信号槽连接, 收到数据时执行slotRec
 *
 * @param reciever 槽对象
 * @param slotRec  槽函数
 */
void TcpServer::connectRec(QObject *reciever, const char *slotRec)
{
    this->connect(this,SIGNAL(sglDataRec(QString)),reciever,slotRec);
}
/**
 * @brief 简化信号槽连接, 有新client连接时执行slotRec
 *
 * @param reciever 槽对象
 * @param slotRec  槽函数
 */
void TcpServer::connectClientConnected(QObject *reciever, const char *slotRec)
{
    this->connect(this,SIGNAL(sglOneClientConnected(QString)),reciever,slotRec);
}
/**
 * @brief 简化信号槽连接, 有 client断开连接时执行slotRec
 *
 * @param reciever 槽对象
 * @param slotRec  槽函数
 */
void TcpServer::connectClientDisconnected(QObject *reciever, const char *slotRec)
{
    this->connect(this,SIGNAL(sglOneClientDisconnected(QString)),reciever,slotRec);
}

/**
 * @brief 读接收的数据, 须配合connectRec
 *
 * @return QByteArray
 */
QByteArray TcpServer::read()
{
    return this->curClient->read();
}

void TcpServer::close()
{
    this->QTcpServer::close();
}

/************************************slots***********************************************/
/**
 * @brief 内部槽, 负责信号转发, 对外封闭, 为了配合connectRec
 *
 * @param clientID
 */
void TcpServer::dataReceived(int clientID)
{
    QString peerFullAddrStr;
    TcpSocketClient *client;
    client = this->mapClientId2Client.value(clientID);
    peerFullAddrStr = client->getPeerFullAddrStr();
    emit sglDataRec(peerFullAddrStr);
}

/**
 * @brief 内部槽, 负责信号转发, 对外封闭, 为了配合connectClientDisconnected
 *
 * @param clientID
 */
void TcpServer::oneClientDisconnected(int clientID)
{
    TcpSocketClient *client;
    QString peerFullAddrStr;
    client = this->mapClientId2Client.value(clientID);
    this->mapClientId2Client.remove(clientID);
    peerFullAddrStr = client->getPeerFullAddrStr();
    this->mapIpFull2Client.remove(peerFullAddrStr);
    delete client;
    emit sglOneClientDisconnected(peerFullAddrStr);
}
