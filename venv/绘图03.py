#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 15:48
# @Author  : chenchao
# @File    : 绘图03.py.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QBrush
#笔刷绘图
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("笔刷绘图")
    def paintEvent(self, QPaintEvent):
        #创建Qpainter对象
        q = QPainter()
        q.begin(self)
        self.drawRectangles(q)
        q.end()
        pass
    def drawRectangles(self,qp):
        #设置画笔颜色,用于画出边框
        qp.setPen(QColor(255,0,0))
        #设置笔刷颜色并画出三个矩形
        qp.setBrush(QColor(100,50,50,10))
        #第四个颜色参数代表透明度，数值越小透明度越高
        qp.drawRect(10,15,90,60)
        #左顶点+长+宽
        qp.setBrush(QColor(10, 255, 100,30))
        qp.drawRect(130, 15, 90, 60)
        qp.setBrush(QColor(25, 100, 50))
        qp.drawRect(250, 15, 90, 60)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())