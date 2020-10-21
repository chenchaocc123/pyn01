#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 15:39
# @Author  : chenchao
# @File    : 绘图02.py
# @Software: PyCharm
import sys,random
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QPen
from PyQt5.QtCore import Qt
# 绘制点图
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("绘制点图")
    def paintEvent(self, QPaintEvent):
        q_painter = QPainter()
        q_painter.begin(self)
        self.drawPoints(q_painter)
        q_painter.end()
    def drawPoints(self,q_painter):
        q_painter.setPen(Qt.red)
        #设置画笔颜色
        size = self.size()
        #窗体大小
        for i in range(1000):
            x=random.randint(1,size.width()-1)
            y=random.randint(1,size.height()-1)
            q_painter.drawPoint(x,y)
            #drawPoint()方法绘制点
        #随机绘制1000个点
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())