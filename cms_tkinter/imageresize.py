from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk

imgpath=""
img=""
myimg=""

def setimage():
    global imgpath, img, myimg
    img = Image.open(imgpath)
    myimg = ImageTk.PhotoImage(img)
    lbl.config(image=myimg)

def saveAs():
    global imgpath
    filepath=tkinter.filedialog.askopenfilenames()
    imgpath=filepath[0]
    setimage()


root=Tk()
root.minsize(300, 200)
root.title("image")
a=10
mainmenu=Menu(root)
submenu=Menu(mainmenu)
mainmenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Save as..", command=saveAs)
root.config(menu=mainmenu)
lfrme=LabelFrame(root, text="hey", width=68, height=68)
lfrme.pack()

lbl=Label(lfrme)
lbl.pack()
#setimage()
root.mainloop()
