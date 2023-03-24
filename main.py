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
# from colorama import Fore, Back, Style
# import asyncio

# # def dialog():
# #     file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
# #                                                "", "Text Files (*.txt)")
# #     if check:
# #         print(Fore.BLUE + "file input path > " + file)

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
        pbar = QProgressBar()
        
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        
        self.setLayout(layout)
        
        self.setFixedSize(400, 600)
        self.setWindowTitle("signC")
        
        self.worker1 = Worker(lambda: createParameter())
        self.worker1.finished.connect(self.on_worker1_finished)
        
        self.worker2 = Worker(lambda: signC(".\\file_input\\in.txt", ".\\file_signed\\s.txt"))
        self.worker2.finished.connect(self.on_worker2_finished)
        
        self.worker3 = Worker(lambda: un_signC(".\\file_signed", ".\\file_unsigned"))
        self.worker3.finished.connect(self.on_worker3_finished)
        
        self.button1 = QPushButton('Create Parameters')
        self.button1.clicked.connect(self.start_task1)
        layout.addWidget(self.button1)
        
        self.button2 = QPushButton('Sign')
        self.button2.clicked.connect(self.start_task2)
        layout.addWidget(self.button2)
        
        self.button3 = QPushButton('un-Sign')
        self.button3.clicked.connect(self.start_task3)
        layout.addWidget(self.button3)
        
    def start_task1(self):
        self.button1.setEnabled(False)
        self.worker1.start()
        
    def on_worker1_finished(self, result):
        self.button1.setEnabled(True)
        
    def start_task2(self):
        self.button2.setEnabled(False)
        self.worker2.start()
        
    def on_worker2_finished(self, result):
        self.button2.setEnabled(True)
        
    def start_task3(self):
        self.button3.setEnabled(False)
        self.worker3.start()
        
    def on_worker3_finished(self, result):
        self.button3.setEnabled(True)
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()