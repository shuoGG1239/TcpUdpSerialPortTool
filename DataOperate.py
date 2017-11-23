from enum import Enum
import re


class HexOrChar(Enum):
    HEX_STYLE = 0
    CHAR_STYLE = 1


class DataOperate():
    @staticmethod
    def splitBySpace(srcString):
        resultList = re.split(r"\s+", srcString.strip())
        return resultList

    @staticmethod
    def hexStringTochars(srcString):
        """
        被空格分隔开的十六进制hex文转为十六进制数组
        :param srcString:
        :return: hex bytearray
        """
        if srcString.strip() == "":
            return bytearray()
        hexStringList = DataOperate.splitBySpace(srcString)
        hexarray = list(map(lambda x: int(x, 16), hexStringList))
        try:
            hexarray = bytearray(hexarray)
        except ValueError as e:
            hexarray = bytearray()
        return hexarray

    @staticmethod
    def charsToHexString(data):
        """
        bytearray转带空格间隔的十六进制string
        :param data: bytearray
        :return: str
        """
        hexStrList = list(map(lambda x: hex(x).replace('0x', '').zfill(2).upper(), data))
        return " ".join(hexStrList) + " "
