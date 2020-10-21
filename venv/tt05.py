#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 20:55
# @Author  : chenchao
# @File    : tt05.py.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


# 消息框重写closeEvent方法
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("消息框重写closeEvent方法")
        self.show()
        # 设置位置和大小
        # 设置窗口标题

    # 重写窗体closeEvent方法
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出', 'are you sure 退出?',
           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            #注意Yes 开头大写
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec())
