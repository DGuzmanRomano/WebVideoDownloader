from tkinter import *
from tkinter import filedialog





def get_path():
    path= filedialog.askdirectory()
    path_label.config(text=path)

root = Tk()
root.title('Video downloader')

canvas = Canvas(root,width=400, height = 300)
canvas.pack()



#app label
app_label = Label (root, text = "Video downloader", fg = "blue", font= ('Arial'))



canvas.create_window(200,20,window=app_label)


#entry to accpet URL

url_entry = Entry(root)
url_label= Label(root, text="Enter video URL")


canvas.create_window(200,80,window=url_label)

canvas.create_window(200,100,window=url_entry)

#path to download

path_label = Label(root,text="Select path to download")
path_button = Button(root,text="Select", command=get_path)


canvas.create_window(200,150,window=path_label)

canvas.create_window(200,170,window=path_button)


#Download Button
download_button = Button(text='Download')

canvas.create_window(200,250,window=download_button)


root.mainloop()