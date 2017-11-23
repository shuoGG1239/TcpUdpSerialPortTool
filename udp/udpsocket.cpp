#include "udpsocket.h"

UdpSocket::UdpSocket(QObject *parent) :
    QObject(parent)
{
    udpSocket = new QUdpSocket(this);
}

/**
 * @brief 创建udp连接
 *
 * @param localIP
 * @param localPort
 * @return bool
 */
bool UdpSocket::createConnection(const QString &localIP, int localPort)
{
    QHostAddress localaddr;
    bool isOK;
    localaddr.setAddress(localIP);
    this->setLocalIp(localIP);
    this->setLocalPort(localPort);
    isOK = udpSocket->bind(localaddr, localPort);
    return isOK;
}

/**
 * @brief 各种发送函数的重载
 *
 * @param data
 */
void UdpSocket::send(QByteArray &data)
{
    QHostAddress dstAddress;
    dstAddress.setAddress(this->getDstIp());
    udpSocket->writeDatagram(data, data.length(), dstAddress, this->getDstPort());
}

void UdpSocket::send(const QString &dataStr)
{
    QHostAddress dstAddress;
    QByteArray data;
    dstAddress.setAddress(this->getDstIp());
    data = dataStr.toLatin1();
    udpSocket->writeDatagram(data, data.length(), dstAddress, this->getDstPort());
}

void UdpSocket::send(QByteArray &data, const QString &dstIp, int dstPort)
{
    QHostAddress dstAddress;
    dstAddress.setAddress(dstIp);
    udpSocket->writeDatagram(data, data.length(), dstAddress, dstPort);
}

void UdpSocket::send(const QString &dataStr, const QString &dstIp, int dstPort)
{
    QHostAddress dstAddress;
    QByteArray data;
    dstAddress.setAddress(dstIp);
    data = dataStr.toLatin1();
    udpSocket->writeDatagram(data, data.length(), dstAddress, dstPort);
}

/**
 * @brief 简化版信号槽连接
 *
 * @param reciever
 * @param slotRec
 */
void UdpSocket::connectRec(QObject *reciever, const char *slotRec)
{
    this->connect(udpSocket,SIGNAL(readyRead()),reciever,slotRec);
}


/**
 * @brief 读数据,须配合connectRec
 *
 * @return QByteArray
 */
QByteArray UdpSocket::read()
{
    QByteArray datagram;       //存放对方发的数据包
    QHostAddress senderAddress;//存放对方的地址
    quint16 senderPort;        //存放对方的端口
    while(udpSocket->hasPendingDatagrams())
    {
        datagram.resize(udpSocket->pendingDatagramSize());  //根据收到的数据定数组容器长度
        udpSocket->readDatagram(datagram.data(),datagram.size(),&senderAddress,&senderPort);//读取数据第一种方法,参考TCP为第二种;UDP不能用readAll
        this->setRecSrcIp(senderAddress.toString());
        this->setRecSrcPort((int)senderPort);
    }
    return datagram;
}

void UdpSocket::close()
{
    udpSocket->close();
}
