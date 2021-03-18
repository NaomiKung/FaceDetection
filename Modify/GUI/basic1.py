from tkinter import *
from tkinter import messagebox
import sys

def mHello():
    print("Hello Every one")

def hello(event):
    status = messagebox.askyesno(title="Show text", message="Hello User!!")
    if status == 0:
        print("Press NO")
    else:
        sys.exit()

gui = Tk()
gui.geometry("500x500")
gui.title("Attendance System")

mlabel =  Label(text="Hello World", fg="red", bg="black").pack()

mButton = Button(text="Submit", fg="blue", bg="white", command=mHello).pack()
b1 = Button(text="Hello")
b1.bind('<Double-1>', hello)
b1.pack()

objEntry = Entry().pack()

menubar = Menu(gui)
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save as")
fileMenu.add_command(label="Close")
menubar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menubar, tearoff=0)
helpMenu.add_command(label="Contract")
helpMenu.add_command(label="Documents")
menubar.add_cascade(label="help", menu=helpMenu)


gui.config(menu=menubar)
gui.mainloop()