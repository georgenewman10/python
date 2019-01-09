from tkinter import *

def doNothing():
    print('printing nothing')

root = Tk()

## Main menu ##

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="new project...", command=doNothing)
subMenu.add_command(label="new...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)


## Toolbar ##

toolbar = Frame(root, bg="blue")

insertBut = Button(toolbar, text="insert image", command=doNothing)
insertBut.pack(side=LEFT, padx=2, pady=5)
printBut = Button(toolbar, text="Print", command=doNothing)
printBut.pack(side=LEFT)

toolbar.pack(size=TOP)



root.mainloop()
