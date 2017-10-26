#ifndef DATAOPERATE_H
#define DATAOPERATE_H

#include <QStringList>

/**
 * @brief 对数据进行一些特殊处理,归类这些操作函数
 *
 */
class DataOperate
{
public:
    enum HexOrChar
    {
        HEX_STYLE=0,
        CHAR_STYLE=1,
    };
    DataOperate();

    QStringList hexStingList;

    static QStringList spliteBySpace(QString srcString); //声明加static,定义时不能加static
    static QByteArray hexStringTochars(QString srcString);
    static QString charsToHexString(QByteArray mydata);

private:

};

#endif // DATAOPERATE_H
