#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 10:59
# @Author  : chenchao
# @File    : 控件02.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QFrame,QPushButton,\
    QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import  QColor
#开关按钮
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("开关按钮")
        self.q_color = QColor(0, 0, 0)
        #创建组件
        buttonr = QPushButton('red', self)
        buttonb = QPushButton('blue', self)
        buttong = QPushButton('green', self)
        buttonr.setCheckable(True)
        buttonb.setCheckable(True)
        buttong.setCheckable(True)
        #创建颜色窗体
        self.qframe = QFrame(self)
        self.qframe.setStyleSheet('QFrame{background:%s}'%self.q_color.name())
        #布局
        qh_box_layout = QHBoxLayout()
        qv_box_layout = QVBoxLayout()
        qv_box_layout.addWidget(buttonr)
        qv_box_layout.addWidget(buttong)
        qv_box_layout.addWidget(buttonb)
        qh_box_layout.addLayout(qv_box_layout)
        qh_box_layout.addWidget(self.qframe)
        self.setLayout(qh_box_layout)
        #添加事件
        buttonr.clicked[bool].connect(self.setColor)
        buttong.clicked[bool].connect(self.setColor)
        buttonb.clicked[bool].connect(self.setColor)

    def setColor(self,pressed):
        source=self.sender()
        #获取信号源
        if pressed:
            val=255
        else:
            val=0
        if source.text()=='red':
            self.q_color.setRed(val)
        elif source.text()=='green':
            self.q_color.setGreen(val)
        elif source.text()=='blue':
            self.q_color.setBlue(val)
        self.qframe.setStyleSheet('QFrame {background-color:%s}'%self.q_color.name())
        print(self.q_color.name())
        ##00ffff
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())
