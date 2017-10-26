#include "configfileshuogg.h"

ConfigFileshuoGG::ConfigFileshuoGG(const QString &configFileUrl)
{
    configFile = new QSettings(configFileUrl, QSettings::IniFormat);
}

ConfigFileshuoGG::~ConfigFileshuoGG()
{
    delete configFile;
}



/**
 * @brief 保存键和值
 *
 * @param key
 * @param value
 */
void ConfigFileshuoGG::setValue(const QString &key, const QString &value)
{
    configFile->setValue(key, value);
}

/**
 * @brief 保存键和值
 *
 * @param key
 * @param value
 */
void ConfigFileshuoGG::setValue(const QString &key, int value)
{
    configFile->setValue(key, value);
}

/**
 * @brief 根据键获取值
 *
 * @param key
 * @return QString
 */
QString ConfigFileshuoGG::getValueString(const QString &key)
{
    return configFile->value(key).toString();
}

/**
 * @brief 根据键获取值
 *
 * @param key
 * @return int
 */
int ConfigFileshuoGG::getValueInteger(const QString &key)
{
    return configFile->value(key).toInt();
}
