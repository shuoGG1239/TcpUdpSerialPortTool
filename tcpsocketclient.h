#ifndef TCPSOCKETCLIENT_H
#define TCPSOCKETCLIENT_H
/*-----------------------------------------------------------------------------------------
 *                                  使用帮助
 * TcpSocketClient:
             使用方法:
                    连接:
                        bool isConnectOK;
                        tcpSocketClient = new TcpSocketClient(this);
                        tcpSocketClient->connectRec(this, SLOT(dataReceivedTCP_client()));
                        isConnectOK = tcpSocketClient->createConnection("192.168.1.101", 5001);
                    发送:
                        tcpSocketClient->send(mybytearray);
                    接收:
                        void TcpUdpComTool::dataReceivedTCP_client()
                        {
                            QByteArray data;
                            data = tcpSocketClient->read();
                        }

------------------------------------------------------------------------------------------*/
#include <QObject>
#include <QTcpSocket>
#include "dataoperate.h"
#include "icommunicatetcpip.h"

class TcpSocketClient : public QObject, public ICommunicateTCPIP
{
    Q_OBJECT
public:
    explicit TcpSocketClient(QObject *parent = 0);
    ~TcpSocketClient();

    virtual bool createConnection(const QString &ip, int port);
    virtual void send(QByteArray &data);
    virtual void send(const QString &dataStr);
    virtual QByteArray read();
    void close();
    virtual void connectRec(QObject *reciever, const char *slotRec);
    void connectRecWithClientID(QObject *reciever, const char *slotRec);
    void connectDisconnectWithClientID(QObject *reciever, const char *slotRec);


    bool setSocketDescriptor(int socketDescriptor);

    void connectClientDisconnect(QObject *reciever, const char *slotRec);

    void setIsConnected(bool isConnected)
    {
        this->isConnected = isConnected;
    }
    bool getIsConnected()
    {
        return isConnected;
    }
    void setTcpClientID(int tcpClientID)
    {
        this->tcpClientID = tcpClientID;
    }
    int getTcpClientID()
    {
        return tcpClientID;
    }
    void setPeerFullAddrStr(const QString &peerFullAddrStr)
    {
        this->peerFullAddrStr = peerFullAddrStr;
    }
    QString getPeerFullAddrStr()
    {
        return peerFullAddrStr;
    }
    QString getPeerIp()
    {
        return tcpSocketClient->peerAddress().toString();
    }
    int getPeerPort()
    {
        return (int)(tcpSocketClient->peerPort());
    }

private:
    QTcpSocket *tcpSocketClient;
    bool isConnected;
    int  tcpClientID;
    QString peerFullAddrStr;

signals:
    void readyReadClientID(int clientId);
    void disconnectedClientID(int clientId);

private slots:
    void dataReceived();
    void disConnected();

};

#endif // TCPSOCKETCLIENT_H
