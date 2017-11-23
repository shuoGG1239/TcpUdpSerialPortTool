#ifndef UDPSOCKET_H
#define UDPSOCKET_H
/*-----------------------------------------------------------------------------------------
 *                                  使用帮助
 * UdpSocket:
             使用方法:
                    连接:
                          UdpSocket *udpSocket = new UdpSocket(this);
                          udpSocket->createConnection("192.168.1.100", 5001); //本地Ip和端口
                          udpSocket->connectRec(this,SLOT(dataReceivedUDP())); //接收绑定
                    发送:
                          udpSocket->send(mybytearray, "192.168.1.103", 5003); //目的Ip和端口
                    接收:
                          void TcpUdpComTool::dataReceivedUDP() //接收slot
                          {
                               QByteArray data = udpSocket->read();
                          }

------------------------------------------------------------------------------------------*/
#include <QObject>
#include <QUdpSocket>
#include "../icomm/icommunicatetcpip.h"

class UdpSocket : public QObject, public ICommunicateTCPIP
{
    Q_OBJECT
public:
    explicit UdpSocket(QObject *parent = 0);
    virtual bool createConnection(const QString &localIP, int localPort);
    virtual void send(QByteArray &data);
    virtual void send(const QString &dataStr);
    void send(const QString &dataStr, const QString &dstIp, int dstPort);
    void send(QByteArray &data, const QString &dstIp, int dstPort);
    virtual QByteArray read();
    virtual void connectRec(QObject *reciever, const char *slotfunc);
    void close();

private:
    QUdpSocket *udpSocket;

signals:

public slots:

};

#endif // UDPSOCKET_H
