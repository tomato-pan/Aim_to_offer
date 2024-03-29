from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QLabel, QInputDialog, QLineEdit, QGridLayout, QApplication, QMessageBox)
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
import re
import time


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    @staticmethod
    def intToip(x):
        s = []
        for i in range(4):
            s.append(str(int(x % 256)))
            x /= 256
        return '.'.join(s[::-1])

    @staticmethod
    def ipToint(ip):
        # print(ip)
        s = ip.split('.')[::-1]
        num = 0
        for i in range(4):
            num += int(s[i]) * 256 ** i
        return num

    @staticmethod
    def timeToint(stime):
        # print(ip)
        fa = time.strptime(stime, "%Y-%m-%d %H:%M:%S")
        time1 = time.mktime(fa)
        return int(time1 * 1000)

    @staticmethod
    def intTotime(num):
        num = num / 1000
        print(num)

        stime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(num))
        return stime

    def initUI(self):
        layout = QGridLayout()
        self.setGeometry(500, 500, 400, 200)
        self.setWindowTitle('IP_to_INT')
        self.calButton = QPushButton("ip_to_int")
        self.calButton.clicked.connect(self.get_int)
        self.cal1Button = QPushButton("int_to_ip")
        self.cal1Button.clicked.connect(self.get_ip)
        self.cal2Button = QPushButton("time_to_int")
        self.cal2Button.clicked.connect(self.get_time)
        self.cal3Button = QPushButton("int_to_time")
        self.cal3Button.clicked.connect(self.get_int_time)
        self.cal4Button = QPushButton("Byte_to_MB")
        self.cal4Button.clicked.connect(self.get_byte)
        self.cal5Button = QPushButton("MB_to_Byte")
        self.cal5Button.clicked.connect(self.get_mb)
        self.cancelButton = QPushButton("退出", self)
        self.cancelButton.clicked.connect(QCoreApplication.instance().quit)

        IPLabel = QLabel("IP:")
        self.IpValue = QLineEdit(self)
        INTLabel = QLabel("Int:")
        self.IntValue = QLineEdit(self)
        TimeLabel = QLabel("Time:")
        self.TimeValue = QLineEdit(self)
        TintLabel = QLabel("Tint:")
        self.TintValue = QLineEdit(self)
        ByteLabel = QLabel("Byte:")
        self.ByteValue = QLineEdit(self)
        MbLabel = QLabel("MB:")
        self.MbValue = QLineEdit(self)


        layout.addWidget(IPLabel, 1, 0)
        layout.addWidget(self.IpValue, 1, 1)
        layout.addWidget(INTLabel, 2, 0)
        layout.addWidget(self.IntValue, 2, 1)
        layout.addWidget(self.TimeValue, 3, 1)
        layout.addWidget(TimeLabel, 3, 0)
        layout.addWidget(self.TintValue, 4, 1)
        layout.addWidget(TintLabel, 4, 0)
        layout.addWidget(self.ByteValue, 5, 1)
        layout.addWidget(ByteLabel, 5, 0)
        layout.addWidget(self.MbValue, 6, 1)
        layout.addWidget(MbLabel, 6, 0)

        layout.addWidget(self.calButton, 1, 2)
        layout.addWidget(self.cal1Button, 2, 2)
        layout.addWidget(self.cal2Button, 3, 2)
        layout.addWidget(self.cal3Button, 4, 2)
        layout.addWidget(self.cal4Button, 5, 2)
        layout.addWidget(self.cal5Button, 6, 2)
        layout.addWidget(self.cancelButton, 7, 1)
        self.setLayout(layout)

        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def get_byte(self):
        if self.ByteValue.text():
            Byte = self.ByteValue.text()  # 获取文本框byte
            try:
                Byte=int(Byte)
                MB = Byte/1024/1024
                self.MbValue.setText(str(round(MB,2)))
            except:
                QMessageBox.critical(self, "错误", "请输入正确byte数！")
                self.ByteValue.clear()
        else:
            QMessageBox.critical(self, "错误", "请输入byte数！")

    def get_mb(self):
        if self.MbValue.text():
            Mb = self.MbValue.text()  # 获取文本框MB
            try:
                Mb = float(Mb)
                Byte = Mb*1024 * 1024
                self.ByteValue.setText(str(Byte))
            except:
                QMessageBox.critical(self, "错误", "请输入正确MB数！")
                self.ByteValue.clear()
        else:
            QMessageBox.critical(self, "错误", "请输入MB数！")

    def get_int(self):
        if self.IpValue.text():
            IP = self.IpValue.text()  # 获取文本框IP
            parttern = '^(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\d)\\.(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\.(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)\\.(1\\d{2}|2[0-4]\\d|25[0-5]|[1-9]\\d|\\d)$'
            if re.match(parttern, IP):
                Int = Example.ipToint(str(IP))
                self.IntValue.setText(str(Int))
            else:
                QMessageBox.critical(self, "错误", "请输入正确的IP！")
                self.IpValue.clear()
            # self.IpValue.clear()
        else:
            QMessageBox.critical(self, "错误", "请输入IP！")

    def get_ip(self):
        if self.IntValue.text():
            Int = self.IntValue.text()
            if re.match(r"^\d+$", Int) and int(Int) <= 4294967295:
                Int = Example.intToip(int(Int))
                self.IpValue.setText(str(Int))
            else:
                QMessageBox.critical(self, "错误", "请输入正确的Int！")
                self.IntValue.clear()
            # self.IntValue.clear()
        else:
            QMessageBox.critical(self, "错误", "请输入Int！")

    def get_time(self):
        if self.TimeValue.text():
            Time = self.TimeValue.text()  # 获取文本框IP
            parttern = r'^\d{4}[-]([0][1-9]|(1[0-2]))[-]([1-9]|([012]\d)|(3[01]))([ \t\n\x0B\f\r])(([0-1]{1}[0-9]{1})|([2]{1}[0-4]{1}))([:])(([0-5]{1}[0-9]{1}|[6]{1}[0]{1}))([:])((([0-5]{1}[0-9]{1}|[6]{1}[0]{1})))$'
            print(re.match(parttern, Time))
            if re.match(parttern, Time):
                Int = Example.timeToint(str(Time))
                self.TintValue.setText(str(Int))
            else:
                QMessageBox.critical(self, "错误", "请输入正确的time, ！%Y-%m-%d %H:%M:%S")
                self.TimeValue.clear()
            # self.IpValue.clear()
        else:
            QMessageBox.critical(self, "错误", "请输入time！")

    def get_int_time(self):
        if self.TintValue.text():
            Int = self.TintValue.text()
            if re.match(r"^\d+$", Int) and 0 <= int(Int) <= 2147483648999:
                Time = Example.intTotime(int(Int))
                self.TimeValue.setText(Time)
            else:
                QMessageBox.critical(self, "错误", "请输入正确的TInt！")
                self.TintValue.clear()
        else:
            QMessageBox.critical(self, "错误", "请输入TInt！")
import hashlib
def get_file_md5(file_path):
    """
    获取文件md5值
    :param file_path: 文件路径名
    :return: 文件md5值
    """
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        _hash = md5obj.hexdigest()
    return str(_hash).lower(),len(str(_hash))

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ex = Example()
    # sys.exit(app.exec_())
    print(get_file_md5("f:/download/SecureLink-2.9.0-1035-1540-win-ia32.exe"))
    print(get_file_md5("f:/download/SecureLink-2.9.0-1035-1540-win-x64.exe"))
