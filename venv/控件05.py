#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 17:14
# @Author  : chenchao
# @File    : 控件05.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,\
    QCalendarWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QDate
#日期组件
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("日期组件")
        #添加组件
        q_calendar = QCalendarWidget(self)
        q_calendar.setGridVisible(True)
        #设置网格可见
        self.q_label = QLabel(self)
        data=q_calendar.selectedDate()
        self.q_label.setText(str(data))
        #设置布局
        layout = QVBoxLayout()
        layout.addWidget(q_calendar)
        layout.addWidget(self.q_label)
        self.setLayout(layout)
        #添加信号
        q_calendar.clicked[QDate].connect(self.showDate)
    def showDate(self,data):
        self.q_label.setText(str(data))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())