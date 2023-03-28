from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import uic
import sys

class MainWindow(QtCore):
    def __init__(self) -> None:
        super().__init__()  
        
    def run(self):
        uic.loadUi("./main.ui")
        

if __name__ == "__main__":
    app = MainWindow([])
    app.run()