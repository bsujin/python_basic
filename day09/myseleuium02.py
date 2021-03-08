import sys
from selenium import webdriver
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("button.ui")[0]

browser = webdriver.Chrome()
browser.get("http://localhost:8081/HELLOWEB01/mycrawl")

    
class WindowClass(QMainWindow, form_class):

    def __init__(self):
#         print(":1!")
        super().__init__()
#         print(":2!")
        self.setupUi(self)
#         print(":3!")
        self.pb.clicked.connect(self.pb_click)
#         print(":4!")

    def pb_click(self):
#         print("click")
        browser.get("http://localhost:8081/HELLOWEB01/mylogin")
        browser.get("http://localhost:8081/HELLOWEB01/mycrawl")
#         text = browser.select("td")
        # td값을 출력하기 
        menus = browser.find_elements_by_css_selector('td')
        for i in menus:
            print(i.text)

if __name__ == "__main__":  
    app = QApplication(sys.argv)
#     print(":1")
    myWindow = WindowClass()
#     print(":2")
    myWindow.show()
#     print(":3")
    app.exec_()
#     print(":4")
  

# 로그인 후 실행하면 들어가질 수 있다
# QT를 사용하여 로그인 처리하기 

