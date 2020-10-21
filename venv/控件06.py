#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 18:34
# @Author  : chenchao
# @File    : 控件06.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QHBoxLayout
from PyQt5.QtGui import QPixmap
# QPixmap组件
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("QPixmap组件")
        #添加组件
        q_pixmap = QPixmap('../img/an03.jpg')
        q_label = QLabel(self)
        q_label.setPixmap(q_pixmap)
        # 优化显示图像
        #新建布局
        layout = QHBoxLayout()
        layout.addWidget(q_label)
        self.setLayout(layout)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())