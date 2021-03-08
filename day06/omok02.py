import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

form_class = uic.loadUiType("omok02.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.icon0 = QIcon('0.png')
        self.icon1 = QIcon('1.png')
        self.icon2 = QIcon('2.png')
        self.arrpb = []
        self.arr2d = [
                        [1,0,1,0,0, 0,0,0,0,0],
                        [0,2,0,2,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0]
                    ]
        
        
        
        for i in range(10):
            for j in range(10):
                button = QPushButton("", self) 
                button.setGeometry(j*40, i*40, 40, 40)
                button.setIconSize(QSize(40, 40))
                button.setIcon(self.icon0) 
                button.clicked.connect(self.pb_click)
                self.arrpb.append(button)
        self.myrender()

    def myrender(self):
        for i in range(10):
            for j in range(10):
                idx = i*10+j
                if self.arr2d[i][j] == 0 :
                    self.arrpb[idx].setIcon(self.icon0) 
                elif  self.arr2d[i][j] == 1 :    
                    self.arrpb[idx].setIcon(self.icon1) 
                elif  self.arr2d[i][j] == 2 :    
                    self.arrpb[idx].setIcon(self.icon2)   

    def pb_click(self) :
        print("pb_click") 
           


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()