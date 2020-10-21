#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 15:21
# @Author  : chenchao
# @File    : 绘图01.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
        \u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
        \u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("绘制文本")
    def paintEvent(self, QPaintEvent):

        q_painter = QPainter()
        q_painter.begin(self)
        self.drawText(QPaintEvent,q_painter)
        q_painter.end()
        #QPainter类负责所有的初级绘制。之间的所有绘画方法去start()和end()方法。
        # 实际的绘画被委托给drawText()方法。
    def drawText(self,event,qp):
        qp.setPen(QColor(255,0,0))
        # 定义画笔
        qp.setFont(QFont('Decorative',10))
        # 定义字体
        qp.drawText(event.rect(),Qt.AlignCenter,self.text)
        # 方法将文本绘制在窗体，显示在中心
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())