#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 21:01
# @Author  : chenchao
# @File    : 拖拽02.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QPushButton,QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return
        # 右击拖动
        data = QMimeData()
        # QDrag提供了对基于MIME的拖放的数据传输的支持。
        q_drag = QDrag(self)
        q_drag.setMimeData(data)
        q_drag.setHotSpot(e.pos() - self.rect().topLeft())
        #topLeft()要大写
        # Drag对象的exec_()方法用于启动拖放操作。
        q_drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:
            # 左键点击
            print('press')


# 拖动按钮
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('dsc ', self)
        self.button.move(100,65)

        self.setWindowTitle("拖动按钮")
        self.setGeometry(300, 300, 300, 200)
        # 接收投放

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.pos()
        self.button.move(pos)
        e.setDropAction(Qt.MoveAction)
        e.accept()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())