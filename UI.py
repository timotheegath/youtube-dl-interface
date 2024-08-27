import sys, os
from typing import List


from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QFileDialog, QDialog, QMessageBox, QVBoxLayout
from PyQt6.QtCore import QFile, QIODevice, QDir, Qt

from PyQt6 import uic
from youtubeController import YoutubeDownloader

class ErrorDialog(QMessageBox):

    def __init__(self, message, parent: QWidget= None) -> None:
        
        super().__init__(parent)
        self.setWindowTitle("HELLO!")
        self.setText(message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.setIcon(QMessageBox.Icon.Critical)
        

        

class DownloaderUI(QMainWindow):
    class DownloadLogger:
        
        def __init__(self, parent) -> None:
            self.parent = parent
        def debug(self, msg):
            # For compatibility with youtube-dl, both debug and info are passed into debug
            # You can distinguish them by the prefix '[debug] '
            if msg.startswith('[debug] '):
                pass
            else:
                self.info(msg)

        def info(self, msg):
            self.parent.StatusText.setText(msg)
            self.parent.StatusText.repaint()
            pass

        def warning(self, msg):

            pass

        def error(self, msg):
            dlg = ErrorDialog(msg, self.parent)
            dlg.exec()
            
            
    logger: "DownloadLogger"
    def __init__(self):
        super().__init__()
        ui_file_name = "main.ui"       

        uic.load_ui.loadUi(ui_file_name, self)
        
        self.videoLink =""
        self.folderSavePath = os.getcwd()
        self.DestinationPath.setText(self.folderSavePath)    
        self.logger = __class__.DownloadLogger(self)
        self.ytDownloader = YoutubeDownloader(self.download_progress_hook, logger=self.logger)
        self.setup_events()
        self.show()

    def download_progress_hook(self, d):
        if d['status'] == 'started':
            self.DownloadProgress.setValue(15)
        if d['status'] == 'processing':
            self.DownloadProgress.setValue(55)
        if d['status'] == 'finished':
            self.DownloadProgress.setValue(100)
            self.StatusText.setText("Done and ready again :)")
    def download_video(self):
        self.videoLink = self.URLField.text()
        self.ytDownloader.download([self.videoLink])

    def choose_file(self):
        self.folderSavePath = QDir.toNativeSeparators(QFileDialog.getExistingDirectory())
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