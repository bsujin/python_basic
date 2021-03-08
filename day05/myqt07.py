import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myqt07.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb_gawi.clicked.connect(self.pbga_click)
        self.pb_bawi.clicked.connect(self.pbba_click)
        self.pb_bo  .clicked.connect(self.pbbo_click)
    
    def pbga_click(self) :
        self.le1.setText("가위")
        self.pb_click()
        
    def pbba_click(self) :
        self.le1.setText("바위")
        self.pb_click()        
    
    def pbbo_click(self) :
        self.le1.setText("보")
        self.pb_click() 
        
    def pb_click(self) :
        mine = self.le1.text()
        com = ""
        rnd = random.randint(1,3)
        if rnd == 1 :
            com = "가위"
        elif rnd == 2 :
            com = "바위"
        else:
            com = "보"
            
        result = ""
        if mine == "가위" and com == "가위" :
            result = "비겼습니다." 
        elif mine == "가위" and com == "바위" :
            result = "졌습니다."
        elif mine == "가위" and com == "보" :
            result = "이겼습니다."    
            
        elif mine == "바위" and com == "가위" :
            result = "이겼습니다." 
        elif mine == "바위" and com == "바위" :
            result = "비겼습니다."
        elif mine == "바위" and com == "보" :
            result = "졌습니다." 
            
        elif mine == "보" and com == "가위" :
            result = "졌습니다." 
        elif mine == "보" and com == "바위" :
            result = "이겼습니다."
        elif mine == "보" and com == "보" :
            result = "비겼습니다."  
        
        self.le2.setText(com)   
        self.le3.setText(result)   


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()