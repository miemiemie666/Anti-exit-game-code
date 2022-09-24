import sys,time 
import pyautogui as pag

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui import Ui_Form

class MyThread(QThread):
    timeTriger = pyqtSignal()

    def __init__(self):
        super(MyThread,self).__init__()

    def run(self):
        while True:
            self.timeTriger.emit()
            time.sleep(120)


class MyMainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        self.__ui = Ui_Form()
        self.__ui.setupUi(self)
                
        self.myThread1 = MyThread()
        self.myThread1.timeTriger.connect(self.inputSignal)

        self.__ui.pushButton.clicked.connect(self.openThread)
        self.__ui.pushButton_2.clicked.connect(self.myclose)

    def openThread(self):
        try:
            self.myThread1.start()
            self.__ui.pushButton.setText("Running")          
        except KeyboardInterrupt:
            print("\nOpen Error.")

    def myclose(self):
        try:
            self.myThread1.terminate() 
            self.__ui.pushButton.setText("Open")       
        except KeyboardInterrupt:
            print("\nClose Error.")

    def inputSignal(self):
        print("press 'm'") 
        pag.press( 'm' )   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())


