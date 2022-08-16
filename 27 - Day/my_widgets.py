from tkinter import *


window = Tk()
window.title("Tkinter Widgets")
window.minsize(width=500, height=500)


# label
label = Label(text="This is Label", font=("Arial", 20, "bold"))
label.pack()

# input
entry = Entry(width=50)
entry.insert(END, string="Enter your name")
entry.focus()
entry.pack()


# button
def fun():
    label.config(text=entry.get())


button = Button(text="Click Me", command=fun)
button.pack()


# text field ( big text field )
text = Text(width=50, height=10)
text.insert(END, "Tell me about yourself")
text.pack()


def text_fun():
    label.config(text=text.get("1.0", END))


text_btn = Button(text="Text Button", command=text_fun)
text_btn.pack()


#   spinbox
def spin_fun():
    label.config(text=spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=20, command=spin_fun)
spinbox.pack()


# scale
def scale_fun(value):
    label.config(text=value)


scale = Scale(from_=0, to=50, command=scale_fun)
scale.pack()


#   checkbutton
def check_fun():
    label.config(text=check_state.get())


check_state = IntVar()
checkbutton = Checkbutton(text="It on?", variable=check_state, command=check_fun)
check_state.get()
checkbutton.pack()


#   radio button
def radio_fun():
    label.config(text=radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Male", variable=radio_state, value=1, command=radio_fun)
radiobutton2 = Radiobutton(text="Female", variable=radio_state, value=2, command=radio_fun)
radiobutton1.pack()
radiobutton2.pack()





















window.mainloop()
