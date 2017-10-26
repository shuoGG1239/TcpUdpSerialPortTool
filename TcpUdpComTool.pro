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
    dataoperate.cpp \
    dialoghelpshortcut.cpp \
    qsssetting.cpp \
    titlebar.cpp \
    qssstyleshuoggdef.cpp \
    configfileshuogg.cpp \
    serialport.cpp \
    udpsocket.cpp \
    tcpsocketclient.cpp \
    tcpserver.cpp

HEADERS  += tcpudpcomtool.h\
    dataoperate.h \
    dialoghelpshortcut.h \
    icommunicate.h \
    qsssetting.h \
    titlebar.h \
    qssstyleshuoggdef.h \
    configfileshuogg.h \
    serialport.h \
    icommunicatetcpip.h \
    udpsocket.h \
    tcpsocketclient.h \
    tcpserver.h

FORMS    += tcpudpcomtool.ui\
    dialoghelpshortcut.ui



OTHER_FILES += \
    ico_set.rc

RC_FILE = ico_set.rc

RESOURCES += \
    qrc.qrc \
