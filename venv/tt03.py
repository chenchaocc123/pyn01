import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QFont
#按钮与悬浮提示
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    #界面初始化
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        #创建一个窗口提示
        btn=QPushButton('小按钮',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        #创建一个按钮提示
        btn.resize(btn.sizeHint())
        #btn.sizeHint()显示默认尺寸
        btn.move(50,50)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltips')
        #设置窗口标题
        pass

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())
