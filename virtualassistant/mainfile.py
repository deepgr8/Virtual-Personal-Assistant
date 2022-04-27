import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from newgui import Ui_MainWindow
import sys
import krishna









class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        krishna.task()


startexe = MainThread()

class graphi_c(QMainWindow):
    def __init__(self):
        super().__init__()

        self.work = Ui_MainWindow()
        self.work.setupUi(self)

        self.work.startbutton.clicked.connect(self.startwork)
        self.work.quitbutton.clicked.connect(self.close)

    def startwork(self, simulator_cal=None):
        self.work.label = QtGui.QMovie("output-onlinegiftools.gif")
        self.work.gif_1.setMovie(self.work.label)
        self.work.label.start()

        self.work.label1 = QtGui.QMovie("output-onlinegiftools (1).gif")
        self.work.gif_2.setMovie(self.work.label1)

        self.work.label1.start()

        self.work.label2 = QtGui.QMovie("initial.gif")
        self.work.gif_3.setMovie(self.work.label2)
        
        self.work.label2.start()

    

        


        startexe.start()









Gui_App = QApplication(sys.argv)

Gui_Jarvis = graphi_c()
# startFunctions = MainThread()


Gui_Jarvis.show()

exit(Gui_App.exec_())
