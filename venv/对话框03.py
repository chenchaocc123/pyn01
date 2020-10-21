#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 8:54
# @Author  : chenchao
# @File    : 对话框.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QFontDialog,\
    QVBoxLayout,QPushButton,QLabel,QSizePolicy
# 字体对话框
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("字体对话框")
        #创建组件
        self.button = QPushButton('改变字体', self)
        self.button.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        #不会拉伸按钮
        self.q_label = QLabel('改变字体', self)
        #创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.q_label)
        self.setLayout(layout)
        #添加信号槽
        self.button.clicked.connect(self.showDialog)
    def showDialog(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.q_label.setFont(font)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())