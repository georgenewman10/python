from tkinter import *
root = Tk()


def printName(event):
    print("George Newman")
     


button_1 = Button(root,text="Print name")
button_1.bind("<Button-1>", printName)  
button_1.pack()



root.mainloop()
