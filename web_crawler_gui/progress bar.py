from tkinter import *
from tkinter import ttk
import threading
val=TRUE
root=Tk()
root.minsize(300, 200)
root.title("progress_bar")
root.wm_iconbitmap('E:\imagesPy\py.ico')

progress_bar=ttk.Progressbar(root, length=200)
progress_bar.pack(pady=30)
progress_bar.start()
progress_bar.step(5)
progress_bar2=ttk.Progressbar(root, length=200)
progress_bar2.pack(pady=40)
progress_bar2.start()

def mainlopping():
    global val
    while(val):
        continue

threadobj=threading.Thread(target=mainlopping)

print(threading.current_thread().getName())



root.mainloop()