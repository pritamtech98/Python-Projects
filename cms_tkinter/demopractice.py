from tkinter import *
import tkinter.ttk

from PIL import Image, ImageTk
def select_list(eve):
    for el in list.curselection():

        print(list.get(el, el)[0])

root=Tk()
root.minsize(100, 80)
btn1=Button(root, text="Button 1")
btn1.pack()

btn2=tkinter.ttk.Button(root, text="Button 2")
btn2.pack()

entry1=Entry(root, width=10)
entry1.pack()
newImage=Image.open("E:\\imagesPy\\Python.jpg")

myimage=ImageTk.PhotoImage(Image.open("E:\\imagesPy\\Python.jpg"))
print(myimage.height())

btn=Button(root, text="hey", image=myimage)
btn.pack()
entry2=tkinter.ttk.Entry(root, width=10)
entry2.pack()

chk1=Checkbutton(root, text="Check1")
chk1.pack()
varChk=IntVar()
chk2=tkinter.ttk.Checkbutton(root, text="Check1", variable=varChk, onvalue=1, offvalue=0, command=lambda : print(varChk.get()))
varChk.set(0)
chk2.pack()

list=Listbox(root, selectmode="extended")
list.insert(END, "apple")
list.insert(END, "mango")
list.insert(END, "orange")
list.bind("<<ListboxSelect>>", select_list)
list.pack()
combo=tkinter.ttk.Combobox(root, values=("mango", "orange", "papaya", "apple"))
combo.pack()

radio=tkinter.ttk.Radiobutton(root, text="radio")
radio.pack()

root.mainloop()