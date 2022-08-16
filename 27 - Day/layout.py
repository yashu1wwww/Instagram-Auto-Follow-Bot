from tkinter import *


window = Tk()
window.title("My First GUI App")
window.minsize(width=600, height=300)
window.config(padx=50, pady=50)


#   METHODS
def entry_text():
    my_label.config(text=entry.get())


def button_clicked():
    my_label.config(text="Button Clicked")


# label component
my_label = Label(text="My First Label", font=("Arial", 20, "bold"))
# my_label.pack(side="left")
# my_label.place(x=10, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)


#   Entry  ( INPUT FIELD )
entry = Entry()
# entry.pack(side="left")
# entry.place(x=10, y=50)
entry.grid(column=3, row=2)


# button
button = Button(text="Click Me", command=entry_text)
# button.pack(side="left")
# button.place(x=10, y=80)
button.grid(column=1, row=1)
button.config(padx=10, pady=10)


#   new button
new_btn = Button(text="New Button")
new_btn.grid(column=2, row=0)
new_btn.config(padx=10, pady=10)






















window.mainloop()
