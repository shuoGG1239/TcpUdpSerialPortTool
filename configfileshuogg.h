#ifndef CONFIGFILESHUOGG_H
#define CONFIGFILESHUOGG_H
/*-----------------------------------------------------------------------------------------
 *                                  使用帮助
 * ConfigFileshuoGG:
                使用方法:
                         ConfigFileshuoGG *myconfig = new ConfigFileshuoGG("condat.ini");
                         myconfig->setValue("age", 22);
                         myconfig->setValue("name", "小明");
                         int myvalue1 = myconfig->getValueInteger("age");
                         QString myvalue2 = myconfig->getValueString("name")

------------------------------------------------------------------------------------------*/
#include <QSettings>

class ConfigFileshuoGG
{
public:
    ConfigFileshuoGG(const QString &configFileUrl);
    ~ConfigFileshuoGG();

    void setValue(const QString &key, const QString &value);
    void setValue(const QString &key, int value);
    QString getValueString(const QString &key);
    int getValueInteger(const QString &key);


private:
    QSettings *configFile;

};

#endif // CONFIGFILESHUOGG_H
