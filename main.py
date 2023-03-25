from cypher import createParameter, signC, un_signC
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QFrame,
    QFileDialog,
    QVBoxLayout,
    QProgressBar,
    QWidget,
    QStatusBar
)
import sys
import functools
from colorama import Fore, Back, Style
# import asyncio

class Worker(QThread):
    finished = pyqtSignal(str)
    
    def __init__(self, function):
        super().__init__()
        self.function = function
    
    def run(self):
        result = self.function()
        self.finished.emit(result)
        
# def dialog():
#     file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
#                                             "", "Text Files (*.txt)")
#     if check:
#         print(Fore.BLUE + "file input path > " + file)

class dialog(QFileDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        file, check = QFileDialog.getOpenFileName(None, "Open File to SignC", "", "Text Files (*.txt)")
        
        if check:
            print(file)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
       
        
        
        self.pbar = QProgressBar()   # progress bar
        layout = QVBoxLayout()
        self.create_btn = QPushButton("Create Parameter")
        self.sign_btn = QPushButton("Sign")
        self.unsign_btn = QPushButton("un-Sign")
        
        # init worker for multi-processing
        self.wCP = Worker(lambda: createParameter(160))
        self.wCP.finished.connect() # when wCP finished work, this will call a function
        self.wSign = Worker(lambda: signC())
        self.wSign.finished.connect() # when wSign finished work, this will call a function 
        self.wUnSign = Worker(lambda: un_signC())
        self.wUnSign.finished.connect() # when wUnSign finished work, this will call a function
        
        self.create_btn.clicked.connect()
                
        self.setFixedSize(400, 500)
        self.setLayout(layout)
        self.setWindowTitle("signC")
        # self.setLayoutDirection(layout)
              
        layout.addWidget(self.create_btn)
        layout.addWidget(self.sign_btn) 
        layout.addWidget(self.unsign_btn)
        layout.addWidget(self.pbar)
        
    def create_P(self):
        # sth here
        self.create_btn.setDisabled(True)
        self.wCP.start()
        
        
        
        
        
    # def UIComponent(self):
        # add widget here!
        
        
        
        
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()