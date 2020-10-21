#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 9:16
# @Author  : chenchao
# @File    : 对话框04.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTextEdit,QAction,QFileDialog
from PyQt5.QtGui import QIcon
#文件对话框
class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("文件对话框")
        #添加组件
        self.textEdit=QTextEdit()
        self.setCentralWidget(self.textEdit)
        #将文本编辑器添加到窗体中央
        self.statusBar()
        #添加事件
        q_action = QAction(QIcon('../img/zhtz1.png'), '打开', self)
        q_action.setShortcut('ctr+q')
        q_action.setStatusTip('open new file')
        q_action.triggered.connect(self.showDialog)

        bar = self.menuBar()
        menu_bar = bar.addMenu('df')
        menu_bar.addAction(q_action)
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, '看文件', '../img')
        # 第一个参数父窗体，第二个参数对话框标题，第三个参数文件路径,后面还可以添加过滤器
        if fname[0]:
            print(fname)
            # ('C:/mycode/PYqt5/pyn01/img/ggg.txt', 'All Files (*)')
            print(fname[0])
            #C:/mycode/PYqt5/pyn01/img/ggg.txt
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                print(data)
                self.textEdit.setText(data)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())