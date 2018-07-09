## TcpUdpSerialPortTool
Tcp+Udp+串口的调试工具, 可以随意定制, 目的是在不改代码重新发布的情况下可以现场调整测试需求;

## 平台
* 原版本为Qt5-C++版本,在cpp_ver分支中, 完成了作为Tcp+Udp+串口的通信基本功能, 可以作为一个稳定的普通工具来使用
* 现主分支为PyQt5重写版, 新加了AOP功能, 完善中

## 依赖
* python3
* pyQt5
* QCandyUi

## 基础功能
* Udp + TcpClient + TcpServer + SerialPort
![tool](https://i.loli.net/2018/07/06/5b3f66e24719f.png)
<br><br>

## AOP功能
* 下面的例子表示将每次接收到数据转发到192.168.75.111:7777(Udp)
![aop](https://i.loli.net/2018/07/06/5b3f670bd5354.png)


