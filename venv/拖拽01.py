#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 20:20
# @Author  : chenchao
# @File    : 拖拽01.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,\
    QVBoxLayout,QPushButton,QLineEdit
# 拖放
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("拖放")
        #添加组件
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        #支持拖走
        button = Button('gbd', self)
        #设置布局
        layout = QVBoxLayout()
        layout.addWidget(edit)
        layout.addWidget(button)
        self.setLayout(layout)


class Button(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setAcceptDrops(True)
        #支持投下
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            #只接收文本,注意不要敲错了
            e.accept()
        else:
            e.ignore()
    #投下事件
    def dropEvent(self, e):
        self.setText(e.mimeData().text())



if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())