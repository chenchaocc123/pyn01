#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 19:09
# @Author  : chenchao
# @File    : 信号槽04.py.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSignal,QObject
#QObject发出信号
class Coo(QObject):
    closeApp=pyqtSignal()
    #closeApp是一个信号
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("QObject发出信号")
        #创建信号对象
        self.s=Coo()
        #连接信号槽
        self.s.closeApp.connect(self.close)
    def mousePressEvent(self, QMouseEvent):
        self.s.closeApp.emit()
        #在窗口中按下鼠标，激活信号

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())