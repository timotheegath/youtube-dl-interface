
from PyQt6.QtWidgets import QMainWindow
from views.MainViewTemplate import Ui_MainWindow
from PyQt6.uic import load_ui



class DownloaderUI(QMainWindow, Ui_MainWindow):
    
    def __init__(self, root: str, load_dev_ui: bool = False):
        super().__init__()
        if load_dev_ui:
            ui_file_name = "./views/main.ui"       

            load_ui.loadUi(ui_file_name, self)
        else:
            self.setupUi(self)
        self.DestinationPath.setText(root)    

