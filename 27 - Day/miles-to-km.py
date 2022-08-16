from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def converter():
    convert = float(entry.get()) * 1.609
    result.config(text=round(convert))


entry = Entry()
entry.grid(column=1, row=0)


miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10)


is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10, pady=10)


result = Label(text="0")
result.grid(column=1, row=1)
result.config(padx=10, pady=10)


km = Label(text="Km")
km.grid(column=2, row=1)
km.config(padx=10, pady=10)


button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)




















window.mainloop()
