#include "dialoghelpshortcut.h"
#include "ui_dialoghelpshortcut.h"

DialogHelpShortcut::DialogHelpShortcut(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogHelpShortcut)
{
    ui->setupUi(this);
    this->setWindowTitle("Help");
    this->setFixedSize(240,320);
}

DialogHelpShortcut::~DialogHelpShortcut()
{
    delete ui;
}
