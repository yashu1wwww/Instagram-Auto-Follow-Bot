from tkinter import *


window = Tk()


a_label = Label(bg="blue", width=40, height=10)
a_label.grid(row=0, column=1, columnspan=3)

b_label = Label(bg="red", width=20, height=10)
b_label.grid(row=1, column=1)

c_label = Label(bg="green", width=40, height=10)
c_label.grid(row=2, column=0, columnspan=2)

d_label = Label(bg="yellow", width=20, height=10)
d_label.grid(row=3, column=3)










































window.mainloop()
