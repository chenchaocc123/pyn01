#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 15:28
# @Author  : chenchao
# @File    : 布局03.py.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QPushButton
#表格布局
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("网格布局")
        #创建网格布局
        q_grid_layout = QGridLayout()
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions=[(i,j) for i in range(5) for j in range(4)]
        for name,position in zip(names ,positions):
            #zip对应打包，大致长（‘cls',(0,0))这样，一一对应
            #然后name,position一一赋值
            if name=='':
                continue
            button = QPushButton(name)
            q_grid_layout.addWidget(button,*position)
            #*position对元组进行解包，分别入参
        #循环创建按钮并添加
        #设置窗口布局
        self.setLayout(q_grid_layout)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())