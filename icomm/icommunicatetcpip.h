#ifndef ICOMMUNICATETCPIP_H
#define ICOMMUNICATETCPIP_H

#include <QString>
#include <QHostInfo>
#include <QHostAddress>
#include <QAbstractSocket>
#include <QStringList>
#include "icommunicate.h"

class ICommunicateTCPIP:public ICommunicate
{
public:
    virtual bool createConnection(const QString &ip, int port) = 0;
    virtual void send(QByteArray &data) = 0;
    virtual void send(const QString &dataStr) = 0;
    virtual QByteArray read() = 0;
    virtual void connectRec(QObject *reciever, const char *slotfunc) = 0;

    static QStringList getLocalIpList()
    {
        QStringList ipList;
        QHostInfo myHostInfo=QHostInfo::fromName(QHostInfo::localHostName());//本地信息获取
        foreach(QHostAddress myaddr,myHostInfo.addresses())
        {
            if(myaddr.protocol()==QAbstractSocket::IPv4Protocol)
            {
                ipList.append(myaddr.toString());
            }
        }
        return ipList;
    }

    void setLocalIp(const QString &ip)
    {
        localIp = ip;
    }
    void setDstIp(const QString &ip)
    {
        dstIp = ip;
    }
    void setLocalPort(int port)
    {
        localPort = port;
    }
    void setDstPort(int port)
    {
        dstPort = port;
    }
    QString getLocalIp()
    {
        return localIp;
    }
    QString getDstIp()
    {
        return dstIp;
    }
    int getLocalPort()
    {
        return localPort;
    }
    int getDstPort()
    {
        return dstPort;
    }

    QString getRecSrcIp()
    {
        return recSrcIp;
    }
    int getRecSrcPort()
    {
        return recSrcPort;
    }
    void setRecSrcIp(const QString &ip)
    {
        recSrcIp = ip;
    }
    void setRecSrcPort(int port)
    {
        recSrcPort = port;
    }

private:
    QString localIp;
    int localPort;
    QString dstIp;
    int dstPort;
    QString recSrcIp;
    int recSrcPort;



};

#endif // ICOMMUNICATETCPIP_H
