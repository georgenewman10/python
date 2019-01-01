from tkinter import *


class Mybuttons:
    
    def __init__(self, master):
        frame = Frame(master, width=400, height=400)
        frame.pack()
        
        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("message")
        


root = Tk()

b = Mybuttons(root)

root.mainloop()
