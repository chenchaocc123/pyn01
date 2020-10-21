#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 17:29
# @Author  : chenchao
# @File    : 绘图05.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QBrush
from PyQt5.QtCore import Qt
# 笔刷
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("笔刷")
    def paintEvent(self, QPaintEvent):
        q_painter = QPainter()
        q_painter.begin(self)
        self.drawBrush(q_painter)
        q_painter.end()
    def drawBrush(self,q):
        bursh=QBrush(Qt.SolidPattern)
        q.setBrush(bursh)
        q.drawRect(10,15,90,60)
        bursh=QBrush(Qt.Dense1Pattern)
        q.setBrush(bursh)
        q.drawRect(130,15,90,60)
        bursh=QBrush(Qt.Dense2Pattern)
        q.setBrush(bursh)
        q.drawRect(250,15,90,60)
        bursh=QBrush(Qt.DiagCrossPattern)
        q.setBrush(bursh)
        q.drawRect(10,105,90,60)
        bursh=QBrush(Qt.Dense5Pattern)
        q.setBrush(bursh)
        q.drawRect(130,105,90,60)
        bursh=QBrush(Qt.Dense6Pattern)
        q.setBrush(bursh)
        q.drawRect(250,105,90,60)
        bursh=QBrush(Qt.HorPattern)
        q.setBrush(bursh)
        q.drawRect(10,195,90,60)
        bursh=QBrush(Qt.VerPattern)
        q.setBrush(bursh)
        q.drawRect(130,195,90,60)
        bursh=QBrush(Qt.BDiagPattern)
        q.setBrush(bursh)
        q.drawRect(250,195,90,60)

        pass
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())