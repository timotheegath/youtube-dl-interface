from app.app import DownloaderApplication
import sys



app = DownloaderApplication(sys.argv)

sys.exit(app.exec())