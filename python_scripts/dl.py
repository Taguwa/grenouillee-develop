from yt_dlp import YoutubeDL

# ダウンロードしたい動画のyoutubeのurl(複数指定可能）
urls = ["https://youtu.be/gaf-u4arvZ0","https://youtu.be/IxMKeRBOUXY"]

# 設定(mp3形式にするなど）
ydl_opts = {
    "format": "mp3/bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        }
    ],
}

# ダウンロード
with YoutubeDL(ydl_opts) as ydl:
    result = ydl.download(urls)