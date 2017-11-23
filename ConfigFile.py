import json

class ConfigFile:
    """
    实现setValue和getValue都是独立的操作,虽然每次操作都要对文件进行读写,会比较慢
    """
    def __init__(self, configFileUrl):
        self.configFile = json.load(open(configFileUrl))
        self.filename = configFileUrl

    def setValue(self, key, value):
        self.configFile[key] = value
        with open(self.filename, 'w') as jsonfile:
            jsonfile.write(json.dumps(self.configFile))

    def getValue(self, key):
        self.refresh()
        return self.configFile.get(key)

    def refresh(self):
        self.configFile = json.load(open(self.filename))


