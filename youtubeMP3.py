import yt_dlp

SAVE_PATH = "./songs/"

mode = input("Select Mode :\n1.From songURL.text\n2.From url input\nEnter mode (1 or 2): ")

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": f"{SAVE_PATH}%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

match mode:
    case "1":
        with open("songURL.txt", "r") as file:
            for i, url in enumerate(file):
                try:
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    print("Downloaded and converted to MP3 successfully!")
                except Exception as e:
                    print(f"An error occurred: {e}")
    case "2":
        url = input("Enter YouTube URL: ")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Downloaded and converted to MP3 successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
    case default:
        print("Invalid input!")