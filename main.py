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

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        pbar = QProgressBar()   # progress bar
        layout = QVBoxLayout()
        create_btn = QPushButton(self)
        sign_btn = QPushButton(self)
        unsign_btn = QPushButton(self)

        self.setLayout(layout)
        
        layout.addWidget(self.create_btn)
        layout.addWidget(self.sign_btn) 
        layout.addWidget(self.unsign_btn)
        
        
        
        
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()