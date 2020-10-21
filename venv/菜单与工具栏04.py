#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 18:21
# @Author  : chenchao
# @File    : 菜单与工具栏.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTextEdit,QAction
from PyQt5.QtGui import QIcon
class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("菜单与工具栏")
        #添加事件
        q_action = QAction(QIcon('../img/zhtz1.png'), 'Exit', self)
        q_action.setShortcut('Ctrl+Q')
        q_action.setStatusTip('Exit application')
        q_action.triggered.connect(self.close)
        #另一种关闭窗口方法qApp.quit
        self.statusBar()
        #创建菜单栏
        menu_bar = self.menuBar()
        #添加菜单
        add_menu = menu_bar.addMenu('渣渣')
        #设置菜单栏的名字
        #添加事件
        add_menu.addAction(q_action)
        #创建工具栏
        tool_bar = self.addToolBar('呱呱呱')
        #设置工具栏的名字
        tool_bar.addAction(q_action)
        #添加事件

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())