#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 15:10
# @Author  : chenchao
# @File    : 布局02.py.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout
#框布局
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        button1 = QPushButton("bt1")
        button2 = QPushButton("bt2")
        #添加组件
        layout1 = QHBoxLayout()
        layout1.addStretch(1)
        # 添加伸缩因子，用来填充空白区域
        layout1.addWidget(button1)
        layout1.addWidget(button2)

        qv_box_layout = QVBoxLayout()
        qv_box_layout.addStretch(1)
        # 添加伸缩因子，填充空白区域
        qv_box_layout.addLayout(layout1)

        self.setLayout(qv_box_layout)
        #设置窗口布局
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("框布局")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())