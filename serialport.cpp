#include "serialport.h"

QStringList SerialPort::baudList;
Init init;

SerialPort::SerialPort(QObject *parent):QObject(parent)
{
    serialPort = new QSerialPort(this);
}

SerialPort::~SerialPort()
{
}

/**
 * @brief 获取pc中可连接的com
 *
 * @return QStringList
 */
QStringList SerialPort::getSerialPortList()
{
    QStringList strList;
    foreach(const QSerialPortInfo &SerialPortInfo,QSerialPortInfo::availablePorts())
    {
        strList.append(SerialPortInfo.portName());
    }
    return strList;
}


/**
 * @brief 简化版槽函数
 *
 * @param reciever
 * @param slotRec
 */
void SerialPort::connectRec(QObject *reciever, const char *slotRec)
{
    this->connect(serialPort,SIGNAL(readyRead()),reciever,slotRec);
}


/**
 * @brief 打开指定端口的串口
 *
 * @param port
 * @param baudRate
 * @return bool
 */
bool SerialPort::openPort(const QString &port, int baudRate)
{
    bool isOpenSuccess;
    serialPort->setPortName(port);
    isOpenSuccess = (serialPort->open(QIODevice ::ReadWrite)
                     //串口参数设置
                     &&serialPort->setBaudRate(baudRate)
                     &&serialPort->setDataBits(QSerialPort::Data8)
                     &&serialPort->setDataErrorPolicy(QSerialPort::IgnorePolicy)
                     &&serialPort->setFlowControl(QSerialPort::NoFlowControl)
                     &&serialPort->setParity(QSerialPort::NoParity)
                     &&serialPort->setStopBits(QSerialPort::OneStop));
    return isOpenSuccess;
}

/**
 * @brief 发送函数及其各种重载
 *
 * @param dataStr
 */
void SerialPort::send(const QString &dataStr)
{
    serialPort->write(dataStr.toLatin1());
}

void SerialPort::send(QByteArray &data)
{
    serialPort->write(data);
}

/**
 * @brief 接收数据, 须配合connectRec
 *
 * @return QByteArray
 */
QByteArray SerialPort::read()
{
    return serialPort->readAll();
}

/**
 * @brief 获取当前连接的串口名
 *
 * @return QString
 */
QString SerialPort::getCurPortName()
{
    return serialPort->portName();
}

void SerialPort::close()
{
    serialPort->close();
}
