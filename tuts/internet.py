from tkinter import *
window = Tk()
window.title('Window Title')
window.geometry("700x400+400+200")

lbl = Label(window, text="hello")
lbl.grid(row=0, column=0)




window.mainloop()
