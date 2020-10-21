#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 19:45
# @Author  : chenchao
# @File    : 对话框01.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,\
    QInputDialog,QHBoxLayout
#输入对话框
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("设置标题")
        #新建组件
        self.edit = QLineEdit(self)
        self.button = QPushButton('修改',self)
        #布局
        layout = QHBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        #连接信号槽
        self.button.clicked.connect(self.showText)
    def showText(self):
        text,ok=QInputDialog.getText(self,'对话框标题','对话框消息')
        #ok为布尔型变量
        if ok:
            self.edit.setText(text)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())