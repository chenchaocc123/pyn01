#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 13:43
# @Author  : chenchao
# @File    : 控件03.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QSlider,QLabel,\
    QLineEdit,QHBoxLayout,QVBoxLayout,QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QColor
#滑块组件
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("滑块组件")
        #添加组件
        self.q_color = QColor(0, 0, 0)
        self.q_labelr = QLabel('红色：',self)
        self.q_sliderr = QSlider(Qt.Horizontal,self)
        self.editr = QLineEdit(self)
        self.q_labelg = QLabel('绿色：',self)
        self.q_sliderg = QSlider(Qt.Horizontal,self)
        self.editg = QLineEdit(self)
        self.q_labelb = QLabel('蓝色：',self)
        self.q_sliderb = QSlider(Qt.Horizontal,self)
        self.editb = QLineEdit(self)
        self.q_frame = QFrame(self)
        self.q_frame.setStyleSheet('QFrame{background:%s}'%self.q_color.name())
        #设置布局
        layout1 = QHBoxLayout()
        layout1.addWidget(self.q_labelr)
        layout1.addWidget(self.q_sliderr)
        layout1.addWidget(self.editr)
        layout2 = QHBoxLayout()
        layout2.addWidget(self.q_labelg)
        layout2.addWidget(self.q_sliderg)
        layout2.addWidget(self.editg)
        layout3 = QHBoxLayout()
        layout3.addWidget(self.q_labelb)
        layout3.addWidget(self.q_sliderb)
        layout3.addWidget(self.editb)
        #局部布局
        layout = QVBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        #总体布局
        layout4 = QVBoxLayout()
        layout4.addLayout(layout)
        layout4.addWidget(self.q_frame)
        self.setLayout(layout4)
        #添加信号
        self.q_sliderr.valueChanged.connect(self.changeValuer)
        self.q_sliderg.valueChanged.connect(self.changeValueg)
        self.q_sliderb.valueChanged.connect(self.changeValueb)
    def changeValuer(self,value):
        self.q_color.setRed(value)
        self.q_frame.setStyleSheet('QFrame {background-color:%s}' % self.q_color.name())
        print(value)
        #value为int型要转成String类型
        self.editr.setText(str(value))
        pass
    def changeValueg(self,value):
        self.q_color.setGreen(value)
        self.q_frame.setStyleSheet('QFrame {background-color:%s}' % self.q_color.name())
        self.editg.setText(str(value))
        pass
    def changeValueb(self,value):
        self.q_color.setBlue(value)
        self.q_frame.setStyleSheet('QFrame {background-color:%s}' % self.q_color.name())
        self.editb.setText(str(value))
        pass


if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())