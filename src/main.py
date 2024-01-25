from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import * 
from PyQt5.QtGui import *
from PyQt5 import QtGui
import sys
from pathlib import Path

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.init_ui()

        self.current_file = None

    def init_ui(self):
        # Body
        self.setWindowTitle("PyQt Text Editor")
        self.resize(1300, 900)

        # Load stylesheet from file
        self.setStyleSheet(open("./src/css/style.qss", "r").read())

        # Alternative Consolas Font
        self.window_font = QFont("Fira Code")
        self.window_font.setPointSize(12)
        self.setFont(self.window_font)

        # Set up menu and body
        self.set_up_menu()
        self.set_up_body()

        self.show()

    def get_editor(self) -> QsciScintilla:
        pass

    def set_up_menu(self):
        # Add menu setup code here
        menu_bar = self.menuBar()

        # File menu 
        file_menu = menu_bar.addMenu("File")

        new_file = file_menu.addAction("New")
        new_file.setShortcut("Ctrl+N")
        new_file.triggered.connect(self.new_file)

        open_file = file_menu.addAction("Open File")
        open_file.setShortcut("Ctrl+O")
        open_file.triggered.connect(self.open_file)

        open_folder = file_menu.addAction("Open Folder")
        open_folder.setShortcut("Ctrl+O")
        open_folder.triggered.connect(self.open_folder)

        # edit menu 
        edit_menu = menu_bar.addMenu("Edit")
        
        copy_action = edit_menu.addAction("Copy")
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.copy)
        # TODO: add more here

    def new_file(self):
        ''''''
    
    def open_file(self):
        ''''''

    def open_folder(self):
        ''''''

    def copy(self):
        ''''''

    def set_up_body(self):
        # Add body setup code here
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindows()
    sys.exit(app.exec_())
