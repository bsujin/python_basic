import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import random
from astropy.units import ya

form_class = uic.loadUiType("ddong01.ui")[0]

class Pengsu:
    def __init__(self):
        self.i = 2
        self.j = 2
    
    def __str__(self):
        return "i:"+str(self.i)+",j:"+str(self.j)+""



class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.peng2D = [
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0]
                    ]     
        self.dong2D = [
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0]
                    ]                
        self.scrn2D = [
                        [2,0,0,0,0],
                        [0,2,0,0,0],
                        [0,0,1,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0]
                    ]
        self.lbl2D = []
        self.pengsu = Pengsu()
        
        
        self.setupUi(self)
        self.pm0 = QPixmap("image/empty.png")
        self.pm1 = QPixmap("image/pengsu.png")
        self.pm2 = QPixmap("image/ddong.gif")
        
        
        for i in range(5):
            line = []
            for j in range(5):
                lbl = QLabel(self)
                lbl.setGeometry(80*j, 80*i, 80, 80)
                lbl.resize(80,80)   # 이미지를 보여주기 위해 출력될 label의 크기를 400×400으로 설정
                lbl.setScaledContents(True)
                lbl.setPixmap(QPixmap(self.pm2))
                line.append(lbl)
            self.lbl2D.append(line)

        self.setDong2D()
        self.setPeng2D()        
        self.setScrn2D()
        self.myrender()

    def btn_click(self) :
        pass
      
    def setDong2D(self) :
        yabawi = []
        for i in range(25):
            if i != 12 :
                yabawi.append(i)
        
        for i in range(100):
            seed = random.randint(0,25-2)
            orig = yabawi[0]
            mixd = yabawi[seed]
            yabawi[0]       = mixd
            yabawi[seed]    = orig
            
        for  i in range(10):
            ii = int(yabawi[i]/5) 
            jj = yabawi[i]%5
            self.dong2D[ii][jj] = 2 

    
        
    def keyPressEvent(self, e):
        
        orign_i = self.pengsu.i
        orign_j = self.pengsu.j
        
        
        key = e.key()
#         16777235 위 16777237 아래 16777234 좌 16777236 우
        if key == 16777235:
            self.pengsu.i -= 1
        if key == 16777237:
            self.pengsu.i += 1
        if key == 16777234:
            self.pengsu.j -= 1
        if key == 16777236:
            self.pengsu.j += 1   
        
        if (self.pengsu.i<0 or 5<=self.pengsu.i) or (self.pengsu.j<0 or 5<=self.pengsu.j):    
            self.pengsu.i = orign_i
            self.pengsu.j = orign_j
            return   

        self.setPeng2D()        
        self.removeDDong()
        flag_fd = self.isFinalDDong()
        self.setScrn2D()
        
        self.myrender()
        if flag_fd :
            QMessageBox.about(self, "DDong PengSu","Mission Clear..")
        
    def isFinalDDong(self):   
        sum = 0
        for i in range(5):
            for j in range(5):
                sum += self.dong2D[i][j]
        
        if sum == 0 :
            return True
        else :
            return False
        
    def removeDDong(self):    
        if self.dong2D[self.pengsu.i][self.pengsu.j] == 2:
            self.dong2D[self.pengsu.i][self.pengsu.j] = 0
        
    def setScrn2D(self):
        for i in range(5):
            for j in range(5):
                self.scrn2D[i][j] = 0
                
        for i in range(5):
            for j in range(5):
                if self.dong2D[i][j] == 2:
                    self.scrn2D[i][j] = 2
                if self.peng2D[i][j] == 1:
                    self.scrn2D[i][j] = 1
                
        
    def setPeng2D(self):
        for i in range(5):
            for j in range(5):
                self.peng2D[i][j] = 0
        self.peng2D[self.pengsu.i][self.pengsu.j]= 1
        
        
    def myrender(self):
        for i in range(5):
            for j in range(5):
                if self.scrn2D[i][j] == 0:
                    self.lbl2D[i][j].setPixmap(QPixmap(self.pm0))
                if self.scrn2D[i][j] == 1:
                    self.lbl2D[i][j].setPixmap(QPixmap(self.pm1))
                if self.scrn2D[i][j] == 2:
                    self.lbl2D[i][j].setPixmap(QPixmap(self.pm2))



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
