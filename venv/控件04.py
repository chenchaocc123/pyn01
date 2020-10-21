#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 16:28
# @Author  : chenchao
# @File    : 控件04.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,\
    QProgressBar,QVBoxLayout
from PyQt5.QtCore import QBasicTimer
#进度条组件
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("进度条组件")
        self.bar = QProgressBar(self)
        self.button = QPushButton('start', self)
        #布局
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.bar)
        self.setLayout(layout)
        #添加信号
        self.button.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        #创建计时器
        self.step = 0
    def timerEvent(self, e):
        #设置停止时间
        if self.step>=100:
            self.timer.stop()
            self.button.setText('Finished')
            return
        self.step=self.step+1
        self.bar.setValue(self.step)
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('start')
            #开始计时
        else:
            self.timer.start(100,self)
            self.button.setText('stop')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())