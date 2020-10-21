#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 16:33
# @Author  : chenchao
# @File    : 绘图04.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QPen
from PyQt5.QtCore import Qt
#画笔Qpen
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("画笔Qpen")
    def paintEvent(self, QPaintEvent):
        # paintEvent(QPaintEvent *)是系统自动调用的
        q = QPainter()
        q.begin(self)
        self.drawLines(q)
        q.end()
    def drawLines(self,q):
        q_pen = QPen(Qt.red, 3, Qt.SolidLine)
        q.setPen(q_pen)
        q.drawLine(20,40,250,40)
        #两点画线
        q_pen.setStyle(Qt.DashLine)
        q.setPen(q_pen)
        q.drawLine(20,80,250,80)
        q_pen.setStyle(Qt.DashDotLine)
        q.setPen(q_pen)
        q.drawLine(20,120,250,120)
        q_pen.setStyle(Qt.DashDotLine)
        q.setPen(q_pen)
        q.drawLine(20,160,250,160)
        q_pen.setStyle(Qt.DotLine)
        q.setPen(q_pen)
        q.drawLine(20,200,250,200)
        q_pen.setStyle(Qt.CustomDashLine)
        q_pen.setDashPattern([1, 4, 5, 4])
        # 奇数画实线，偶数留空
        q.setPen(q_pen)
        q.drawLine(20, 240, 250, 240)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())