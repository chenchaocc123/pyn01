import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
#导入QIcon包
#更改图标
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,200,220)
        #把窗口大小和位置一起设置
        self.setWindowIcon(QIcon('../img/gg.jpg'))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())