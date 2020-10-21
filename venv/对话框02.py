#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 20:39
# @Author  : chenchao
# @File    : 对话框02.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QFrame,\
    QColorDialog,QHBoxLayout
from PyQt5.QtGui import QColor
#颜色对话框
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("颜色对话框")
        #添加组件
        self.button = QPushButton('变色', self)
        self.q_frame = QFrame(self)
        q = QColor(0, 0, 0)
        #创建颜色
        self.q_frame.setStyleSheet("QWidget { background-color: %s }" % q.name())
        #初始frame
        self.q_frame.resize(300,300)
        #布局
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.q_frame)
        self.setLayout(layout)
        #连接信号槽
        self.button.clicked.connect(self.showColo)
    def showColo(self):
        col=QColorDialog.getColor()
        if col.isValid():
            #检查col的值是否有效
            self.q_frame.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
        pass
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())
