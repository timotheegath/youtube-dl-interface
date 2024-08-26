import yt_dlp

class YoutubeDownloader(yt_dlp.YoutubeDL):
    def __init__(self, progress_hook=None):
        self.ydl_opts = {
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',        
        }],
        "progress_hooks":[progress_hook]}
        super().__init__(self.ydl_opts)
    def download_to_mp3(self, link):
        self.download([link])
    def change_out_folder(self, new_folder: str):
        self.ydl_opts['paths']={"home": f"{new_folder}"}




if __name__ == "__main__":
    ytdl = YoutubeDownloader()
    ytdl.download_to_mp3('https://youtu.be/1LmX5c7HoUw')