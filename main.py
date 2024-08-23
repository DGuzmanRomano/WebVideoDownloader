from tkinter import *
from tkinter import filedialog

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

root.mainloop()