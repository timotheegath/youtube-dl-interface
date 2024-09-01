.\.venv\Scripts\Activate.ps1
pyuic6 .\views\main.ui -o .\views\MainViewTemplate.py
pyinstaller --onefile --clean main.py