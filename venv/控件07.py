#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 18:43
# @Author  : chenchao
# @File    : 控件07.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,\
    QLineEdit,QLabel,QVBoxLayout
# QlineEdit
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("QlineEdit")
        #添加组件
        self.q_label = QLabel(self)
        self.edit = QLineEdit(self)
        #设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.q_label)
        layout.addWidget(self.edit)
        self.setLayout(layout)
        #添加信号
        self.edit.textChanged[str].connect(self.onChanged)
    def onChanged(self,text):

        self.q_label.setText(text)
        self.q_label.adjustSize()
        #重新调整长度
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())