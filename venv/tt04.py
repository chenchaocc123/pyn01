import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import QCoreApplication
#退出按钮
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #新建按钮
        self.btn=QPushButton('quit',self)
        self.btn.setToolTip("单击退出")
        #添加事件
        self.btn.clicked.connect(lambda :QCoreApplication.instance().quit())
        # self.btn.clicked.connect(QCoreApplication.instance().quit)
        # 通过connect方法连接信号与槽函数或者可调用对象。
        #设置按钮大小
        self.resize(self.btn.sizeHint())
        #移动按钮
        self.btn.move(30,30)
        #设置窗口大小位置
        self.setGeometry(300,300,250,150)
        #设置窗口标题
        self.setWindowTitle("退出按钮")
        pass


if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())