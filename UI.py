import sys, os
from typing import List


from PyQt6.QtWidgets import QApplication, QWidget, QPlainTextEdit, QMainWindow, QFileDialog
from PyQt6.QtCore import QFile, QIODevice

from PyQt6 import uic
from youtubeController import YoutubeDownloader

class DownloaderUI(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file_name = "main.ui"       

        uic.load_ui.loadUi(ui_file_name, self)
        self.ytDownloader = YoutubeDownloader(self.download_progress_hook)
        self.videoLink =""
        self.folderSavePath = os.getcwd()
        self.DestinationPath.setText(self.folderSavePath)    

        self.setup_events()
        self.show()

    def download_progress_hook(self, d):
        if d['status'] == 'started':
            self.DownloadProgress.setValue(15)
        if d['status'] == 'processing':
            self.DownloadProgress.setValue(55)
        if d['status'] == 'finished':
            self.DownloadProgress.setValue(100)
    def download_video(self):
        self.videoLink = self.URLField.text()
        self.ytDownloader.download([self.videoLink])

    def choose_file(self):
        self.folderSavePath = QFileDialog.getExistingDirectory()
        self.DestinationPath.setText(self.folderSavePath)     
        self.ytDownloader.change_out_folder(self.folderSavePath) 

    def setup_events(self):
        self.DownloadButton.clicked.connect(self.download_video)
        self.ChooseFolderButton.clicked.connect(self.choose_file)
        
class DownloaderApplication(QApplication):
    DownloaderWindow : DownloaderUI
    def __init__(self, argv: List[str]) -> None:
        super().__init__(argv)
        self.DownloaderWindow = DownloaderUI()

        

if __name__ == "__main__":
    app = DownloaderApplication(sys.argv)    
    sys.exit(app.exec())