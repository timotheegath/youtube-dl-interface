from PyQt6.QtWidgets import QMessageBox, QWidget, QFileDialog
from PyQt6.QtCore import QDir

class ErrorDialog(QMessageBox):

    def __init__(self, message, parent: QWidget= None) -> None:
        
        super().__init__(parent)
        self.setWindowTitle("HELLO!")
        self.setText(message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.setIcon(QMessageBox.Icon.Critical)

class PickFolderDialog(QFileDialog):

    @staticmethod
    def pick_a_directory(parent: QWidget) -> str:
        return QDir.toNativeSeparators(QFileDialog.getExistingDirectory(parent))
