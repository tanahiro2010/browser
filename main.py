import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
print("googleブラウザを基本として設定しました")
x = input("googleを開きますか？_ y/n >")
def browser(xy):
    #start my_app 
    my_app = QApplication(sys.argv) 
    #open webpage
    initurl = xy

    # setting browser
    browser = QWebEngineView()
    browser.load(QUrl(initurl))        
    browser.resize(1000,600)
    browser.move(100,100)

    browser.show() 
    #sys exit function 
    sys.exit(my_app.exec_())
if x == "y":
    browser("https://www.google.co.jp")
else:
    browser(input("URLを入力 >"))
