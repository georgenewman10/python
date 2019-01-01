from tkinter import *
root = Tk()

def leftClick(event):
    print("Left")

def midClick(event):
    print("Double")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", midClick)
frame.pack()



root.mainloop()
