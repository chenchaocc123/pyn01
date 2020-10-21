#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 20:04
# @Author  : chenchao
# @File    : 控件09.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,\
    QComboBox,QLabel,QVBoxLayout
# QComboBox下拉列表
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("QComboBox下拉列表")
        #添加组件

        box = QComboBox(self)
        box.addItem('gg1')
        box.addItem('gg2')
        box.addItem('gg3')
        box.addItem('gg4')
        self.q_label = QLabel("现在选择：",self)
        #设置布局
        layout = QVBoxLayout()
        layout.addWidget(box)
        layout.addWidget(self.q_label)
        self.setLayout(layout)
        #连接信号
        box.activated[str].connect(self.changeBox)
    def changeBox(self,text):
        self.q_label.setText('现在选择：%s' % text)
        self.q_label.adjustSize()
        pass
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())