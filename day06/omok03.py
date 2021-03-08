import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

form_class = uic.loadUiType("omok03.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.flag_wb = True
        self.icon0 = QIcon('0.png')
        self.icon1 = QIcon('1.png')
        self.icon2 = QIcon('2.png')
        self.arr2dpb = []
        self.arr2d = [
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
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
            line = []
            for j in range(10):
                button = QPushButton("", self) 
                button.setGeometry(j*40, i*40, 40, 40)
                button.setIconSize(QSize(40, 40))
                button.setIcon(self.icon0) 
                button.setToolTip(str(i)+","+str(j))
                button.clicked.connect(self.pb_click)
                line.append(button)
            self.arr2dpb.append(line)
        self.myrender()

    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 0 :
                    self.arr2dpb[i][j].setIcon(self.icon0) 
                elif  self.arr2d[i][j] == 1 :    
                    self.arr2dpb[i][j].setIcon(self.icon1) 
                elif  self.arr2d[i][j] == 2 :    
                    self.arr2dpb[i][j].setIcon(self.icon2)   

    def pb_click(self) :
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2d[i][j] >0 :
            return
        
        stone_info = 0
        if self.flag_wb :
            self.arr2d[i][j]=1
            stone_info = 1
        else:
            self.arr2d[i][j]=2
            stone_info = 2
            
        up = self.getUP(i,j,stone_info)
        dw = self.getDW(i,j,stone_info)
        le = self.getLE(i,j,stone_info)
        ri = self.getRI(i,j,stone_info)
        
        ur = self.getUR(i,j,stone_info)
        ul = self.getUL(i,j,stone_info)
        dr = self.getDR(i,j,stone_info)
        dl = self.getDL(i,j,stone_info)
        
        print("up:",up)
        print("dw:",dw)
        print("le:",le)
        print("ri:",ri)
        
        print("ur:",ur)
        print("ul:",ul)
        print("dr:",dr)
        print("dl:",dl)

            
        self.myrender()
        self.flag_wb = not self.flag_wb
        
    def getUP(self,i,j,stone_info):
        cnt = 0
        while True:
            i -= 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt            
            try:
                if self.arr2d[i][j] == stone_info :
                    cnt += 1
                else :
                    return cnt
            except:
                return cnt
        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    
    
    
    
    
    
    