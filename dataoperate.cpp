#include "dataoperate.h"

DataOperate::DataOperate()
{
}




/**
 * @brief 分离空格组成字符串组
 *
 * @param srcString
 * @return QStringList
 */
QStringList DataOperate::spliteBySpace(QString srcString)
{
    /*按1或n个空格分割*/
    return srcString.trimmed().split(QRegExp(" "),QString::SkipEmptyParts);
}


/**
 * @brief 被空格分隔开的十六进制hex文转为十六进制数组
 *
 * @param srcString
 * @return QByteArray
 */
QByteArray DataOperate::hexStringTochars(QString srcString)
{
    QStringList hexStringList=spliteBySpace(srcString);
    QByteArray hexArray;
    bool okflag;
    for(int i=0;i<hexStringList.size();i++)
    {
        hexArray.append(hexStringList.at(i).toInt(&okflag,16));
    }
    return hexArray;
}


/**
 * @brief u8* 转 带空格间隔的十六进制string
 *
 * @param mydata 数据流
 * @return QString 返回如: 68 12 23 AC C0 形式的QString
 */
QString DataOperate::charsToHexString(QByteArray mydata)
{
    QString mystring;
    uchar ubyte;
    //    foreach (uchar temp, mydata)
    //    {
    //        mystring+=( QString::number((uint)temp,16)+" ");
    //    }
    for(int i=0;i<mydata.size();i++)
    {
        ubyte=(uchar)(mydata.at(i));//转为无符号的
        if(0==ubyte)
            mystring+="00 ";
        else if(15>=ubyte)
            mystring+=("0"+QString::number(ubyte,16).toUpper()+" ");
        else
            mystring+=(QString::number(ubyte,16).toUpper()+" ");
    }
    return mystring;

}
