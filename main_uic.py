from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sys
import logging
from algorithm.cypher import createParameter, signC, un_signC
from UI.main import Ui_MainWindow
from UI.debug_dialog import Ui_Dialog
from sub import Worker, dialog

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()  
        self.logger = logging.getLogger(__name__)
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        
        # on start do sth 
        self.setWindowIcon(QIcon('./assets/key.png'))
        self.setWindowTitle("Chương trình mô phỏng lược đồ ký mã dựa trên Elgamal và Schnorr")
        self.uic.signbtn.setDisabled(True)
        self.uic.unSignbtn.setDisabled(True)
        self.uic.statusbar.showMessage("You must create parameters first!", 0)
        
        
        self.uic.actionDebug.triggered.connect(self.open_debug)
    # def run_parameters(self):
    #     lambda: createParameter(160)
    
    def open_debug(self):
        self.uic_dialog = Ui_Dialog()
        # self.uic.setupUi(self)
        # self.uic_dialog.debugText.setReadOnly(True)
        
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())