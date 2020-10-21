#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 18:42
# @Author  : chenchao
# @File    : 信号槽.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLCDNumber,QSlider,QVBoxLayout
from PyQt5.QtCore import Qt
# 信号槽——滑块事件
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("信号槽——滑块事件")
        #添加两个组件
        qlcd_number = QLCDNumber(self)
        q_slider = QSlider(Qt.Horizontal,self)
        #连接信号槽
        q_slider.valueChanged.connect(qlcd_number.display)
        #设置布局
        layout = QVBoxLayout()
        layout.addWidget(qlcd_number)
        layout.addWidget(q_slider)
        self.setLayout(layout)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())