from tkinter import *

root = Tk()                  

#topFrame = Frame(root)
#topFrame.pack()             # if you want anything to display, you have to place it
#bottomFrame = Frame(root)
#bottomFrame.pack(side=BOTTOM)
#button1 = Button(topFrame,    text="Button 1", fg="red")
#button2 = Button(topFrame,    text="Button 2", fg="green")
#button3 = Button(topFrame,    text="Button 3", fg="blue")
#button4 = Button(bottomFrame, text="Button 4", fg="purple")
#button1.pack(side=LEFT)
#button2.pack(side=LEFT)
#button3.pack(side=LEFT)
#button4.pack(side=RIGHT)

one = Label(root, text="One", bg="red", fg="White")
one.pack()
two = Label(root, text="One", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="One", bg="blue", fg="White")
three.pack(side=LEFT,fill=Y)





root.mainloop()



