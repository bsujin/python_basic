import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("myqt06.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.pbnum_click)
        self.pb2.clicked.connect(self.pbnum_click)
        self.pb3.clicked.connect(self.pbnum_click)
        self.pb4.clicked.connect(self.pbnum_click)
        self.pb5.clicked.connect(self.pbnum_click)
        
        self.pb6.clicked.connect(self.pbnum_click)
        self.pb7.clicked.connect(self.pbnum_click)
        self.pb8.clicked.connect(self.pbnum_click)
        self.pb9.clicked.connect(self.pbnum_click)
        self.pb0.clicked.connect(self.pbnum_click)
        
        self.pbcall.clicked.connect(self.pbcall_click)

    def pbnum_click(self) :
        txt_old = self.le1.text()
        txt_new = self.sender().text()
        self.le1.setText(txt_old+txt_new) 

  
    def pbcall_click(self) :
        QMessageBox.about(self, "Calling", self.le1.text())

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()