from views.dialogs import ErrorDialog, PickFolderDialog
from views.mainView import DownloaderUI
from PyQt6.QtWidgets import QApplication
from typing import List
from app.youtubeController import YoutubeDownloader


class DownloadLogger:
        
        def __init__(self, parent) -> None:
            self.parent = parent
        def debug(self, msg):

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

class DownloaderApplication(QApplication):
    DownloaderWindow : DownloaderUI
    ytDownloaderService: YoutubeDownloader
    def __init__(self, argv: List[str], root:str, load_dev_ui: bool = False) -> None:
        super().__init__(argv)
        self.rootDir = root
        self.DownloaderWindow = DownloaderUI(root=self.rootDir, load_dev_ui=load_dev_ui)
        self.ytDownloaderService = YoutubeDownloader(self.download_progress_hook, logger=DownloadLogger(self.DownloaderWindow), ffmpeg_path=f"{root}\\bin")
        self.setup_events()
        
        self.DownloaderWindow.show()
    
    def download_progress_hook(self, d):
        if d['status'] == 'started':
            self.DownloaderWindow.DownloadProgress.setValue(15)
        if d['status'] == 'processing':
            self.DownloaderWindow.DownloadProgress.setValue(55)
        if d['status'] == 'finished':
            self.DownloaderWindow.DownloadProgress.setValue(100)
            self.DownloaderWindow.StatusText.setText("Done and ready again :)")
    def download_video(self):
        
        self.ytDownloaderService.download([self.DownloaderWindow.URLField.text()])

    def choose_file(self):
        folderSavePath = PickFolderDialog.pick_a_directory(self.DownloaderWindow)
        self.DownloaderWindow.DestinationPath.setText(folderSavePath)     
        self.ytDownloaderService.change_out_folder(folderSavePath) 

    def setup_events(self):
        self.DownloaderWindow.DownloadButton.clicked.connect(self.download_video)
        self.DownloaderWindow.ChooseFolderButton.clicked.connect(self.choose_file)