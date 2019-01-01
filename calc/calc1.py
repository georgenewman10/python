from tkinter import *

window = Tk()
window.title('Calculator')
window.geometry("290x200+400+400")






b1 = Button(window, text=' 1 ', fg='black', bg='white', height=1, width=7
command=)
b1.grid(row=2, column=0)

b2 = Button(window, text=' 2 ', fg='black', bg='white', height=1, width=7)
b2.grid(row=2, column=1)

b3 = Button(window, text=' 3 ', fg='black', bg='white', height=1, width=7)
b3.grid(row=2, column=2)

b4 = Button(window, text=' 4 ', fg='black', bg='white', height=1, width=7)
b4.grid(row=3, column=0)

b5 = Button(window, text=' 5 ', fg='black', bg='white', height=1, width=7)
b5.grid(row=3, column=1)

b6 = Button(window, text=' 6 ', fg='black', bg='white', height=1, width=7)
b6.grid(row=3, column=2)

b7 = Button(window, text=' 7 ', fg='black', bg='white', height=1, width=7)
b7.grid(row=4, column=0)

b8 = Button(window, text=' 8 ', fg='black', bg='white', height=1, width=7)
b8.grid(row=4, column=1)

b9 = Button(window, text=' 9 ', fg='black', bg='white', height=1, width=7)
b9.grid(row=4, column=2)

b0 = Button(window, text=' 0 ', fg='black', bg='white', height=1, width=7)
b0.grid(row=5, column=1)
























window.mainloop()
