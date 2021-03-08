import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

form_class = uic.loadUiType("omok01.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        for i in range(10):
            for j in range(10):
                button = QPushButton("", self) 
                button.setGeometry(j*40, i*40, 40, 40)
                button.setIconSize(QSize(40, 40))
                button.setIcon(QIcon('0.png')) 
                button.clicked.connect(self.pb_click)

        
    def pb_click(self) :
        print("pb_click") 
           


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()