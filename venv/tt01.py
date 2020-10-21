import sys
from PyQt5.QtWidgets import QApplication,QWidget
#新建程序窗口
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250,150)
        self.move(300,300)
        #设置窗体大小和位置
        self.setWindowTitle('simple')
        #设置窗体标题

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec())
    #exec是python2的关键词，python3不是了
    #exit确保应用窗口退出再关闭窗口