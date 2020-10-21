#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 18:52
# @Author  : chenchao
# @File    : 信号槽02.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt
#信号槽————键盘事件
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("信号槽————键盘事件")
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()==Qt.Key_Escape:
            #按下esc会退出
            self.close()
            print(QKeyEvent)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())