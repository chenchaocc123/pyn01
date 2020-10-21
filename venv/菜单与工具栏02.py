#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 16:34
# @Author  : chenchao
# @File    : 菜单与工具栏02.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QAction,qApp,QMainWindow
#导入的aApp指的是全局变量Application
from PyQt5.QtGui import QIcon
#菜单栏
class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("菜单栏")
        #创建事件
        q_action = QAction(QIcon("../img/zhtz1.png"), '&Exit', self)
        q_action.setShortcut('Ctrl+Q')
        q_action.setStatusTip('Exit application')
        #会在底部状态栏进行提示
        q_action.triggered.connect(qApp.quit)

        self.statusBar()
        #创建菜单栏
        bar = self.menuBar()
        #添加菜单
        menu =bar.addMenu('&File')
        #添加事件
        menu.addAction(q_action)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())