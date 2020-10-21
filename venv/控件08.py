#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 18:53
# @Author  : chenchao
# @File    : 控件08.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,\
    QSplitter,QHBoxLayout,QStyleFactory,QFrame,QPushButton
from PyQt5.QtCore import Qt
#QSplitter控件尺寸调整
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("QSplitter控件尺寸调整")
        #添加组件
        q_frame1 = QFrame(self)
        q_frame2 = QFrame(self)
        q_frame3 = QFrame(self)
        #设置窗体类型
        q_frame1.setFrameShape(QFrame.StyledPanel)
        q_frame2.setFrameShape(QFrame.StyledPanel)
        q_frame3.setFrameShape(QFrame.StyledPanel)
        #添加QSplitter组件
        q_splitter1 = QSplitter(Qt.Horizontal)
        q_splitter2 = QSplitter(Qt.Vertical)
        #在QSplitter里面添加组件
        q_splitter1.addWidget(q_frame1)
        q_splitter1.addWidget(q_frame2)
        q_splitter2.addWidget(q_splitter1)
        q_splitter2.addWidget(q_frame3)
        #设置总体布局
        layout = QHBoxLayout()
        layout.addWidget(q_splitter2)
        self.setLayout(layout)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())