#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 19:00
# @Author  : chenchao
# @File    : 信号槽03.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QVBoxLayout,QWidget
#sender信号源
class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("sender信号源")
        #添加组件
        button1 = QPushButton('btn1',self)
        button2 = QPushButton('btn2',self)
        #添加信号槽
        button1.clicked.connect(self.clickButton)
        button2.clicked.connect(self.clickButton)
        #添加布局QMainWindow不支持布局
        # layout = QVBoxLayout()
        # layout.addWidget(button1)
        # layout.addWidget(button2)
        # self.setLayout(layout)
        #添加底部状态栏
        button2.move(0,300)
        self.statusBar()
    def clickButton(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text()+'被按下了')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())