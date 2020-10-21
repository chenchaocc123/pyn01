#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 17:11
# @Author  : chenchao
# @File    : 菜单与工具栏03.py.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow
from PyQt5.QtGui import QIcon
class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("工具栏")
        #新建点击事件
        q_action = QAction(QIcon('../img/zhtz1.png'),'Exit',self)
        q_action.setShortcut('Ctrl+Q')
        q_action.triggered.connect(qApp.quit)
        #添加工具栏
        self.bar = self.addToolBar('Exit')
        self.bar.addAction(q_action)
        #添加工具栏事件
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())