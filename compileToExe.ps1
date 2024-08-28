.\.venv\Scripts\Activate.ps1
pyinstaller --onefile --clean --add-binary "bin/ffmpeg.exe;bin/ffmpeg.exe" --add-binary "bin/ffprobe.exe;bin/ffprobe.exe" main.py