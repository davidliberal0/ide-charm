from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import * 
from PyQt5.QtGui import *
from PyQt5 import QtGui


class MainWindows(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        #body
        self.setWindowTitle("PyQt Text Editor")
        self.resize(1300,900)

    self.window_font = QFont("Fira Code")

