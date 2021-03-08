import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myqt05.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pb_click)
    def pb_click(self) :
        mine = self.le1.text()
        com = ""
        rnd = random.random()
        if rnd > 0.5 :
            com = "홀"
        else:
            com = "짝"
            
        result = ""
        if mine == com :
            result = "이겼습니다." 
            self.le3.setStyleSheet("QLineEdit"
                        "{"
                        "background : green;"
                        "}")            
        else :
            result = "졌습니다."
            self.le3.setStyleSheet("QLineEdit"
                        "{"
                        "background : red;"
                        "}")  
        
        self.le2.setText(com)   
        self.le3.setText(result)   


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()