#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 9:30
# @Author  : chenchao
# @File    : 自定义控件01.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QSlider
from PyQt5.QtCore import QObject,Qt,pyqtSignal
from PyQt5.QtGui import QPainter,QFont,QColor,QPen
#自定义组件
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("自定义组件")
        #添加滑块组件
        q_slider = QSlider(Qt.Horizontal, self)
        q_slider.setFocusPolicy(Qt.NoFocus)
        q_slider.setRange(1,750)
        q_slider.setValue(75)
        q_slider.setGeometry(30,40,150,30)
        self.coo = Coo()
        #添加自定义组件
        self.widget = BurningWidget()
        #设置布局
        qh_box_layout = QHBoxLayout()
        qh_box_layout.addWidget(self.widget)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(q_slider)
        layout.addLayout(qh_box_layout)
        layout.addWidget(self.widget)

        self.setLayout(layout)
        #添加信号
        self.coo.signal[int].connect(self.widget.setValue)
        q_slider.valueChanged[int].connect(self.changValue)
        #也可以q_slider.valueChanged[int].connect(self.widget.setValue)
        # 然后在self.widget.setValue方法中添加self.widget.repaint()
    def changValue(self,value):
        self.coo.signal.emit(value)
        self.widget.repaint()
        pass
class Coo(QObject):
    signal = pyqtSignal(int)
    #发送信号并传递int参数
    pass
class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setMinimumSize(1, 30)
        #改变控件的最小高度
        self.value = 600
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]
    def setValue(self,value):
        self.value = value

    def paintEvent(self, QPaintEvent):
        q_painter = QPainter()
        q_painter.begin(self)
        self.drawWidget(q_painter)
        q_painter.end()

    def drawWidget(self, q):
        q_font = QFont('Serif', 7, QFont.Light)
        q.setFont(q_font)

        size = self.size()
        w = size.width()
        h = size.height()
        step = int(round(w / 10.0))
        # 根据组件大小进行动态调整
        till = int((w / 750.0) * self.value)
        #实际数值
        full = int((w / 750.0) * 700)
        #满容量数值
        #
        if self.value>=700:
            q.setPen(QColor(255, 255, 255))
            # 白色边框
            q.setBrush(QColor(255, 255, 184))
            q.drawRect(0,0,full,h)
            q.setBrush(QColor(255,175,175))
            q.drawRect(full,0,till-full,h)
        else:
            q.setPen(QColor(255, 255, 255))
            # 白色边框
            q.setBrush(QColor(255, 255, 184))
            q.drawRect(0,0,till,h)
        #绘制黑色边框
        q_pen = QPen(QColor(20, 20, 20), 1, Qt.SolidLine)
        q.setPen(q_pen)
        q.setBrush(Qt.NoBrush)
        q.drawRect(0,0,w-1,h-1)

        j=0
        for i in range(step,10*step,step):
            # 绘制刻度
            q.drawLine(i,0,i,5)
            # 获取字体宽度
            metrics = q.fontMetrics()
            width = metrics.width(str(self.num[j]))
            q.drawText(i-width/2,h/2,str(self.num[j]))
            j=j+1
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())