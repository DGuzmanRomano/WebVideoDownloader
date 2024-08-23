from tkinter import *
from tkinter import filedialog
import yt_dlp
import shutil

def download():
    video_url = url_entry.get()
    download_path = path_label.cget("text")
    print('Downloading...')

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloaded_video.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        video_file = ydl.prepare_filename(info_dict)

    shutil.move(video_file, download_path)
    print('Download Complete')

def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

root = Tk()
root.title('Video Downloader')

canvas = Canvas(root, width=400, height=300)
canvas.pack()

# App label
app_label = Label(root, text="Video Downloader", fg="blue", font=('Arial'))
canvas.create_window(200, 20, window=app_label)

# URL entry
url_entry = Entry(root)
url_label = Label(root, text="Enter video URL")
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

# Path selection
path_label = Label(root, text="Select path to download")
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 170, window=path_button)

# Download button
download_button = Button(text='Download', command=download)
canvas.create_window(200, 250, window=download_button)

root.mainloop()
