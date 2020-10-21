#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 9:41
# @Author  : chenchao
# @File    : 控件01.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QCheckBox
from PyQt5.QtCore import Qt
# CheckBox
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("CheckBox")
        #添加组件
        box = QCheckBox('show titlte', self)
        box.toggle()
        #有这一句为勾选状态
        #添加信号
        box.stateChanged.connect(self.changeTitle)
    def changeTitle(self,state):
        if state==Qt.Checked:
            self.setWindowTitle('checked')
        else:
            self.setWindowTitle('unchecked')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())