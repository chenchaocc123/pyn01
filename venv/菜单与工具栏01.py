#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 16:24
# @Author  : chenchao
# @File    : 菜单与工具栏01.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
#状态栏
class Demo(QMainWindow):
    #注意继承的是QMainWindow
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar().showMessage('ready')
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("状态栏")


if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())