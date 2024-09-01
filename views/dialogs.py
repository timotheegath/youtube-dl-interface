from PyQt6.QtWidgets import QMessageBox, QWidget, QFileDialog
from PyQt6.QtCore import QDir

class ErrorDialog(QMessageBox):

    def __init__(self, message, parent: QWidget= None) -> None:
        
        super().__init__(parent)
        self.setWindowTitle("There was an error...")
        self.setText(message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.setIcon(QMessageBox.Icon.Critical)

class PickFolderDialog(QFileDialog):

    @staticmethod
    def pick_a_directory(parent: QWidget) -> str:
        return QDir.toNativeSeparators(QFileDialog.getExistingDirectory(parent, options=QFileDialog.Option.ShowDirsOnly))

class FFMPEG_NotFoundDialog(QMessageBox):

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setWindowTitle("Question")
        self.setInformativeText("Where is \"FFMPEG\" ?")
        self.setText("We could not find the executable \"FFMPEG\" on our own. We need it to convert your favourite tunes to mp3. Could you point us to where it is ?")
        self.setIcon(QMessageBox.Icon.Question)
        self.addButton(QMessageBox.StandardButton.Discard)
        self.pick_file_button = self.addButton("Choose file...", QMessageBox.ButtonRole.AcceptRole)

    def ffmpeg_not_found(self):
        button = self.exec()
        if button == self.pick_file_button:
            PickFFMPEGDialog.pick_ffmpeg(self)

    
class PickFFMPEGDialog(QFileDialog):
    @staticmethod
    def pick_ffmpeg(parent: QWidget, startFolder=None) -> str:
        return QDir.toNativeSeparators(QFileDialog.getOpenFileName(parent, caption="Find the FFMPEG executable", directory=startFolder)[0])