import sys
from selenium import webdriver
from PyQt5.QtWidgets import *
from PyQt5 import uic
import time

form_class = uic.loadUiType("button.ui")[0]

    
class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pb_click)

        self.browser = webdriver.Chrome()
        
        # 자동 로그인
        self.browser.get("http://localhost:8081/HELLOWEB01/mylogin")
        time.sleep(1)
        self.browser.get("http://localhost:8081/HELLOWEB01/mycrawl")
        time.sleep(1)
        
    def pb_click(self):
        print("click")

        # td값을 출력하기 : 버튼을 클릭하면 console에 찍힌다  
        menus = self.browser.find_elements_by_css_selector('td')
        for i in menus:
            print(i.text)


if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()


