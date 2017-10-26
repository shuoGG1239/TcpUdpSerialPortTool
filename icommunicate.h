#ifndef ICOMMUNICATE_H
#define ICOMMUNICATE_H
#include <QByteArray>
#include <QString>
#include <QObject>


class ICommunicate
{
public:
    virtual void send(QByteArray &data) = 0;
    virtual void send(const QString &dataStr) = 0;
    virtual QByteArray read() = 0;
    virtual void connectRec(QObject *reciever, const char *slotfunc) = 0;
};

#endif // ICOMMUNICATE_H
