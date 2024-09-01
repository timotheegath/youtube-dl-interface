# yt-dlp-interface
Implementation of youtube-dl with an interface in Python.
##  Credits
- Credits to the [yt-dlp](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#embedding-yt-dlp) library who powers this very basic GUI.
- Credits to [PyQt6](https://pypi.org/project/PyQt6/) which I used to design the GUI.

# Installation instructions
1. Run `pip install -r requirements.txt`
2. Install `ffmpeg`. Either add it to PATH or put somewhere known. It will be used for post-processing for the [yt-dlp](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#embedding-yt-dlp) library
3. Run `main.py`
4. If prompted, specify the path to `ffmpeg`


# How to edit
## UI
When debugging, pass the parameter `--devmode`. This will ensure:
- The UI is pulled from `main.ui` as opposed to the final `.py` equivalent of it. You can make changes to the .ui files without having to convert it to .py every time. 
The `views/main.ui` file can be opened in designer (`pyqt6-tools designer`) to change the QWidgets. 
# Distribution 
The `compileToExe.ps1` script transforms the `main.ui` file into a .py file to remove dependency on non-py files while building the exe. It will then build the app into a .exe.
## Instructions
1. Run the powershell script compileToExe.ps1
2. Retrieve the executable in the `dist` folder
