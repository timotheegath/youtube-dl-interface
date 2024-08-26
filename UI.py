import sys


from PyQt6.QtWidgets import QApplication, QWidget, QPlainTextEdit, QMainWindow
from PyQt6.QtCore import QFile, QIODevice
from PyQt6 import uic

class Downloader(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file_name = "main.ui"       

        uic.load_ui.loadUi(ui_file_name, self)

        self.set_defaults()
        self.show()
    
    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    downloader = Downloader()
    
    sys.exit(app.exec())