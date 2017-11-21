#-------------------------------------------------
#
# Project created by QtCreator 2017-03-24T13:49:31
#
#-------------------------------------------------

QT       += core gui
QT       += network
QT       += serialport

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = TcpUdpComTool
TEMPLATE = app
CONFIG += c++11


SOURCES += main.cpp\
        tcpudpcomtool.cpp\
    stringutils\dataoperate.cpp \
    dialoghelpshortcut.cpp \
    flatui\qsssetting.cpp \
    flatui\titlebar.cpp \
    flatui\qssstyleshuoggdef.cpp \
    configfileshuogg.cpp \
    serialport\serialport.cpp \
    udp\udpsocket.cpp \
    tcp\tcpsocketclient.cpp \
    tcp\tcpserver.cpp

HEADERS  += tcpudpcomtool.h\
    stringutils\dataoperate.h \
    dialoghelpshortcut.h \
    icomm\icommunicate.h \
    flatui\qsssetting.h \
    flatui\titlebar.h \
    flatui\qssstyleshuoggdef.h \
    configfileshuogg.h \
    serialport\serialport.h \
    icomm\icommunicatetcpip.h \
    udp\udpsocket.h \
    tcp\tcpsocketclient.h \
    tcp\tcpserver.h

FORMS    += tcpudpcomtool.ui\
    dialoghelpshortcut.ui



OTHER_FILES += \
    ico_set.rc

RC_FILE = ico_set.rc

RESOURCES += \
    qrc.qrc \
