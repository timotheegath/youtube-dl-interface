
from PyQt6.QtWidgets import QMainWindow

import os
from PyQt6 import uic


class DownloaderUI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        ui_file_name = "./views/main.ui"       

        uic.load_ui.loadUi(ui_file_name, self)        
        self.DestinationPath.setText(os.getcwd())    

