from UI import Downloader
import sys
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)

downloader = Downloader()
Downloader.show()

sys.exit(app.exec())