#ifndef SERIALPORT_H
#define SERIALPORT_H
/*-----------------------------------------------------------------------------------------
 *                                  使用帮助
 * SerialPort:
             使用方法:
                    连接:
                        serialPort = new SerialPort(this);
                        serialPort->connectRec(this,SLOT(comReadData()));
                        bool isOpenSuccess = serialPort->openPort(ui->comboComNum->currentText(),9600);
                    发送:
                        serialPort->send(mybytearray);
                    接收:
                        void TcpUdpComTool::comReadData()
                        {
                            QByteArray data=serialPort->read();
                        }
------------------------------------------------------------------------------------------*/
#include <QSerialPort>
#include <QSerialPortInfo>
#include <QStringList>
#include "icommunicate.h"

namespace SerialPortBlock {
    class Init;
}

class SerialPort: public QObject,public ICommunicate
{
    Q_OBJECT
public:
    SerialPort(QObject *parent = 0);
    ~SerialPort();
    bool openPort(const QString &port, int baudRate);
    void connectRec(QObject *reciever, const char *slotfunc);
    QStringList getSerialPortList();
    virtual void send(QByteArray &data);
    virtual void send(const QString &dataStr);
    virtual QByteArray read();
    QString getCurPortName();
    void close();

    static QStringList baudList;

private:
    QSerialPort *serialPort;

};


/**
 * @brief C++模拟java的静态代码块
 *
 */
class Init{
public:
    Init()
    {
        SerialPort::baudList<<"1200"<<"2400"<<"4800"<<"9600"<<"14400"
                            <<"19200"<<"38400"<<"57600"<<"115200";
    }

};

#endif // SERIALPORT_H
