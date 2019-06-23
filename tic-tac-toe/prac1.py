from tkinter import *
import tkinter.ttk
from tkinter.messagebox import *
import time
def combo_listener(event):
    print(combo.get())

def win_on_close():
    val=askokcancel("Quit", "Do you really want to quit the game?")
    if(val):
        print("Window closed")
        root.destroy()

root=Tk()

combo=tkinter.ttk.Combobox(root)
combo.pack()
items=['hello', 'banana', 'hey']
combo.config(values=items)
combo.set('banana')
combo.bind("<<ComboboxSelected>>", combo_listener)
root.protocol("WM_DELETE_WINDOW", win_on_close)
root.mainloop()