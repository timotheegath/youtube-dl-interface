import yt_dlp

class YoutubeDownloader(yt_dlp.YoutubeDL):
    def __init__(self, progress_hook, logger, ffmpeg_path: str = None):
        self.ffmpeg_path = ffmpeg_path
        self.ydl_opts = {
        'format': 'm4a/bestaudio/best',
        "logger":logger,
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',        
        }],
        "progress_hooks":[progress_hook]}
        if ffmpeg_path:
            self.ydl_opts["ffmpeg_location"] = ffmpeg_path
        
        super().__init__(self.ydl_opts)
    def download_to_mp3(self, link):
        self.download([link])
    def change_out_folder(self, new_folder: str):
        self.ydl_opts['paths']={"home": f"{new_folder}"}
    def extract_video_info(self, link):
        info = self.extract_info(link, download=False)
    def update_ffmpeg_path(self, new_path) -> None:
        self.ffmpeg_path = new_path
        self.ydl_opts["ffmpeg_location"] = new_path
        super().__init__(self.ydl_opts)
    




if __name__ == "__main__":
    ytdl = YoutubeDownloader()
    ytdl.download_to_mp3('https://youtu.be/1LmX5c7HoUw')
