#include "tcpudpcomtool.h"
#include "titlebar.h"
#include "qssstyleshuoggdef.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Q_INIT_RESOURCE(qrc);
    TcpUdpComTool *toolWidget=new TcpUdpComTool();
    WindowWithTitleBar mainwindow(toolWidget,QssSetting::DARKBLUEGREEN);
    mainwindow.setWindowTitle("Tcp Udp SerialPort Tool");
    mainwindow.setWindowIcon(QIcon(TitleBar::imageroot+"myicon.ico"));
    QssStyleShuoGGDef::setAppGreenStyle();
    mainwindow.show();

    return a.exec();
}
