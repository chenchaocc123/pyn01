#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 16:03
# @Author  : chenchao
# @File    : 布局04.py.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,\
    QLineEdit,QGridLayout,QTextEdit
#多行网格
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("多行网格")
        #添加组件
        q_label1 = QLabel('Title')
        q_label2 = QLabel('Author')
        q_label3 = QLabel('Review')
        edit1 = QLineEdit()
        edit2 = QLineEdit()
        edit3 = QTextEdit()
        #设置布局
        layout = QGridLayout()
        layout.addWidget(q_label1,1,0)
        layout.addWidget(q_label2,2,0)
        layout.addWidget(q_label3,3,0)
        layout.addWidget(edit1,1,1)
        layout.addWidget(edit2,2,1)
        layout.addWidget(edit3,3,1,4,1)
        #多行文本框跨第3个参数行第4个参数列
        #设置窗体布局
        self.setLayout(layout)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())