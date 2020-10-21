#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 14:01
# @Author  : chenchao
# @File    : tt06.py.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget
from PyQt5.QtCore import QRect
#窗口显示在屏幕的中间
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #设置窗口大小
        self.resize(400,200)
        #调用center()方法
        self.center()
        #设置标题
        self.setWindowTitle("窗口居中")
    def center(self):
        #设置窗口居中方法
        qr=self.frameGeometry()
        #获得窗口的框架,PyQt5.QtCore.QRect
        print(type(qr))
        cp=QDesktopWidget().availableGeometry().center()
        # 获得屏幕中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        print(qr.topLeft())
        #顶点移动至框架的左上角

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())