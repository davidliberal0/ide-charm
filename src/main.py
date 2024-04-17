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

        self.side_bar_clr = "#282c34"

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
        open_folder.setShortcut("Ctrl+K")
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
        
        # Application Body
        body_frame = QFrame() 
        body_frame.setFrameShape(QFrame.NoFrame)
        body_frame.setFrameShadow(QFrame.Plain)
        body_frame.setLineWidth(0)
        body_frame.setMidLineWidth(0)
        body_frame.setContentsMargins(0, 0, 0 , 0)
        body_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0 , 0)
        body.setSpacing(0)
        body_frame.setLayout(body)
        
        # Side Bar
        self.side_bar = QFrame()
        self.side_bar.setFrameShape(QFrame.Plain)
        self.side_bar.setFrameShadow(QFrame.Plain)
        self.side_bar.setStyleSheet('''
            background-color: {self.side_bar_clr}; 
        ''')
        side_bar_layout = QHBoxLayout()
        side_bar_layout.setContentsMargins(5, 10, 5, 0)
        side_bar_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.side_bar.setLayout(side_bar_layout)


        body.addWidget(self.side_bar)


        # split view 
        self.hsplit = QSplitter(Qt.Horizontal)

        # frame and layout to hold tree view (fire manager)
        self.tree_frame = QFrame()
        self.tree_frame.setLineWidth(1)
        self.tree_frame.setMaximumWidth(400)
        self.tree_frame.setMinimumWidth(200)
        self.tree_frame.setBaseSize(100, 0)
        self.tree_frame.setContentsMargins(0, 0, 0 , 0)
        tree_frame_layout = QVBoxLayout()
        tree_frame_layout.setContentsMargins(0, 0, 0 , 0)
        tree_frame_layout.setSpace (0)
        self.tree_frame.setStyleSheet('''

            QFrame {
                background-color: #21252b;
                border-radius: 5px;
                border: none;
                padding: 5px;
                color: #D3D3D3;
            }
                                      
            QFrame:hover {
                color: white;
            }
        ''')

        # File system model to appear in tree view 
        self.model = QFileSystemModel()
        self.model.setRootPath(os.getcdw())
        # File system filters
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)

        # Tree View 
        self.tree_view = QTreeView()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindows()
    sys.exit(app.exec_())
