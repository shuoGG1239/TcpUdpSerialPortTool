#ifndef TCPSERVER_H
#define TCPSERVER_H
/*-----------------------------------------------------------------------------------------
 *                                  使用帮助
 * TcpServer:
 *           原理分析: 在 tcpsocketclient.cpp
             使用方法:
                    连接:
                          tcpServer = new TcpServer(this);
                          tcpServer->createConnection("192.168.1.100",5001); //本地ip端口
                          tcpServer->connectClientConnected(this, SLOT(updateClientList(QString)));
                          tcpServer->connectClientDisconnected(this, SLOT(disconnectTCPlist(QString)));
                          tcpServer->connectRec(this, SLOT(dataReceivedTCP_server(QString)));
                    发送:
                          tcpServer->setCurClient(ui->comboBoxClientList->currentText());
                          tcpServer->send(mybytearray);
                    接收:
                          void TcpUdpComTool::dataReceivedTCP_server(QString recFromFullAddr)
                          {
                                QByteArray data;
                                QString uiCurClientFullAddr;
                                uiCurClientFullAddr = ui->comboBoxClientList->currentText();
                                if(uiCurClientFullAddr == recFromFullAddr)
                                {
                                     data = tcpServer->read();
                                }
                          }
------------------------------------------------------------------------------------------*/
#include <QObject>
#include <QTcpServer>
#include <QMap>
#include "tcpsocketclient.h"

class TcpServer : public QTcpServer
{
    Q_OBJECT
public:
    explicit TcpServer(QObject *parent = 0);
    ~TcpServer();
    virtual bool createConnection(const QString &localIP, int localPort);
    virtual void send(QByteArray &data);
    virtual void send(const QString &dataStr);
    void send(const QString &dataStr, const QString &dstIp, int dstPort);
    void send(QByteArray &data, const QString &dstIp, int dstPort);
    virtual QByteArray read();
    virtual void connectRec(QObject *reciever, const char *slotRec);
    void connectClientConnected(QObject *reciever, const char *slotRec);
    void connectClientDisconnected(QObject *reciever, const char *slotRec);
    void close();

    void incomingConnection(int handle);
    void setCurClient(const QString &clientIpPortString);

    static QString toFullAddrStr(const QString &ip, int port);

    TcpSocketClient *getCurClient()
    {
        return curClient;
    }


private:
    int curClientID;
    TcpSocketClient *curClient;
    QMap<int, TcpSocketClient *> mapClientId2Client;
    QMap<QString, TcpSocketClient *> mapIpFull2Client;

signals:
    void sglDataRec(QString peerFullAddrStr);
    void sglOneClientConnected(QString peerFullAddrStr);
    void sglOneClientDisconnected(QString peerFullAddrStr);

public slots:
   void dataReceived(int clientID);
   void oneClientDisconnected(int clientID);

};

#endif // TCPSERVER_H
