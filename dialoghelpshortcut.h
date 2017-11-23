#ifndef DIALOGHELPSHORTCUT_H
#define DIALOGHELPSHORTCUT_H

#include <QDialog>

namespace Ui {
class DialogHelpShortcut;
}

/**
 * @brief 快捷键提示窗口
 *
 */
class DialogHelpShortcut : public QDialog
{
    Q_OBJECT

public:
    explicit DialogHelpShortcut(QWidget *parent = 0);
    ~DialogHelpShortcut();

private:
    Ui::DialogHelpShortcut *ui;
};

#endif // DIALOGHELPSHORTCUT_H
