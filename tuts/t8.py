from tkinter import *


class MyButtons:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="QUIT", command=frame.quit)
        self.quitButton.pack(side=BOTTOM)

    def printMessage(self):
        print("Success")


root = Tk()
b = MyButtons(root)

root.mainloop()
