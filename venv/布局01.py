#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 15:05
# @Author  : chenchao
# @File    : 布局01.py.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
#绝对定位
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        q_label1 = QLabel('t1', self)
        q_label2 = QLabel('t2', self)
        q_label3 = QLabel('t3', self)
        # 添加三个组件

        q_label1.move(15,10)
        q_label2.move(35,40)
        q_label3.move(55,70)
        #定位三个组件

        self.setGeometry(300,300,400,350)
        self.setWindowTitle("绝对定位应用")
        pass

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())