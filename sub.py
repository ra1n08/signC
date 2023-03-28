from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog

class Worker(QThread):
    finished = pyqtSignal(str)
    
    def __init__(self, function):
        super().__init__()
        self.function = function
    
    def run(self):
        result = self.function()
        self.finished.emit(result)
        
class dialog(QFileDialog):
    def __init__(self):
        super().__init__()
        
        file, check = QFileDialog.getOpenFileName(None, "Open File to SignC", "", "Text Files (*.txt)")
        
        if check:
            print(file)