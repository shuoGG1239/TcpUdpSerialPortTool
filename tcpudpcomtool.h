#ifndef TCPUDPCOMTOOL_H
#define TCPUDPCOMTOOL_H

#include <QWidget>
#include <QTcpSocket>
#include <QHostAddress>
#include <QHostInfo>
#include <QTcpServer>
#include <QMessageBox>
#include <QSettings>
#include <QSerialPort>
#include <QSerialPortInfo>
#include <QTimer>
#include "dialoghelpshortcut.h"
#include "configfileshuogg.h"
#include "./serialport/serialport.h"
#include "./udp/udpsocket.h"
#include "./tcp/tcpsocketclient.h"
#include "./tcp/tcpserver.h"
#include "ui_tcpudpcomtool.h"

#define WIN_WIDTH  655
#define WIN_HEIGHT 486


namespace Ui {
class TcpUdpComTool;
}

/**
 * @brief 该工具的主界面
 *
 */
class TcpUdpComTool : public QWidget
{
    Q_OBJECT
public:
    enum connectMode
    {
        UDP_MODE        =0,
        TCP_CLIENT_MODE =1,
        TCP_SERVER_MODE =2,
        SERIAL_PORT_MODE=3,
    };
    explicit TcpUdpComTool(QWidget *parent = 0);
    ~TcpUdpComTool();

    UdpSocket *udpSocket;
    TcpSocketClient *tcpSocketClient;
    TcpServer *tcpServer;
    SerialPort *serialPort;
    ConfigFileshuoGG *myconfig;
    Ui::TcpUdpComTool *ui;

protected:
    virtual void keyPressEvent(QKeyEvent *e);

private:
    TcpUdpComTool(const TcpUdpComTool& cpywidget); //防止默认拷贝构造函数瞎搞
    void configDataInit();
    void configDataSave();
    void comboboxInit();
    void connectUDP();
    void connectTCPserver();
    void connectTCPclient();
    void connectCOM();
    DataOperate::HexOrChar getRadioButtStat();
    DataOperate::HexOrChar getCheckBoxStat();
    inline void recByStyle(QByteArray &bytesData);

    QString   myaddress; //本地IP
    QHostInfo myHostInfo;//本机信息
    QStringList connectModeList;//装填combox里面的东西,使combox所有项有1个对应的数字,方便使用swtich
    QString   oldcomNum;

public slots:
    void on_pushButtonStart_clicked();
    void on_pushButtonSend_clicked();
    void on_pushButtonClearRec_clicked();
    void on_toolButtonShortCut_clicked();
    void dataReceivedUDP();
    void dataReceivedTCP_client();
    void dataReceivedTCP_server(QString recFromFullAddr);

    void disconnectTCPlist(QString fullAddrStr);
    void updateClientList(QString fullAddrStr);

private slots:
    void comboxClicked(const QString &selectedText);
    void comReadData();

    void on_comboBoxLocal_activated(const QString &arg1);

signals:
    void ClientReadData(int clientID,QString IP,int Port,QByteArray data);
    void ClientDisConnect(int clientID,QString IP,int Port);

};

#endif // TCPUDPCOMTOOL_H
