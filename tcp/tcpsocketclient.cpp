#include "tcpsocketclient.h"

TcpSocketClient::TcpSocketClient(QObject *parent) :
    QObject(parent)
{
    tcpSocketClient = new QTcpSocket(this);
    this->setIsConnected(false);
    this->connect(tcpSocketClient,SIGNAL(readyRead()),this,SLOT(dataReceived()));
    this->connect(tcpSocketClient,SIGNAL(readyRead()),this,SLOT(dataReceived()));

}

TcpSocketClient::~TcpSocketClient()
{
}



/**
 * @brief 创建连接
 *
 * @param ip
 * @param port
 * @return bool
 */
bool TcpSocketClient::createConnection(const QString &ip, int port)
{
    bool isOK;
    tcpSocketClient->connectToHost(ip,port); //向目的ip服务器的端口进行连接
    isOK = tcpSocketClient->waitForConnected(2000); //等2s, 若还无法连上服务器就算失败
    this->setIsConnected(isOK);
    return isOK;
}

/**
 * @brief 各种发送重载
 *
 * @param data
 */
void TcpSocketClient::send(QByteArray &data)
{
    tcpSocketClient->write(data);
}

void TcpSocketClient::send(const QString &dataStr)
{
    tcpSocketClient->write(dataStr.toLatin1());

}

/**
 * @brief 简化版信号槽
 *
 * @param reciever
 * @param slotRec
 */
void TcpSocketClient::connectRec(QObject *reciever, const char *slotRec)
{
    this->connect(tcpSocketClient,SIGNAL(readyRead()),reciever,slotRec);
}
void TcpSocketClient::connectClientDisconnect(QObject *reciever, const char *slotRec)
{
    this->connect(tcpSocketClient,SIGNAL(disconnected()),reciever,slotRec);//关闭连接时，发送断开连接信号
}

/**
 * @brief 读取接收数据, 须配合connectRec
 *
 * @return QByteArray
 */
QByteArray TcpSocketClient::read()
{
    QByteArray datagram;        //存放对方发的数据包
    datagram = tcpSocketClient->readAll();   //读取数据的另一种方法,参考UDP为第一种方法
    this->setRecSrcIp(tcpSocketClient->peerAddress().toString());  //获取对方(server)的IP
    this->setRecSrcPort((int)tcpSocketClient->peerPort());//获取对方(server)的port
    return datagram;
}

void TcpSocketClient::close()
{
    tcpSocketClient->close();
}


/**
 * @brief 专门提供给TcpServer使用的
 *
 */
void TcpSocketClient::connectRecWithClientID(QObject *reciever, const char *slotRec)
{
    this->connect(this,SIGNAL(readyReadClientID(int)),reciever,slotRec);
}
void TcpSocketClient::connectDisconnectWithClientID(QObject *reciever, const char *slotRec)
{
    this->connect(this,SIGNAL(disconnectedClientID(int)),reciever,slotRec);
}
bool TcpSocketClient::setSocketDescriptor(int socketDescriptor)
{
    return tcpSocketClient->setSocketDescriptor(socketDescriptor);
}
void TcpSocketClient::dataReceived()
{
    emit readyReadClientID(this->getTcpClientID());
}
void TcpSocketClient::disConnected()
{
    emit disconnectedClientID(this->getTcpClientID());
}
