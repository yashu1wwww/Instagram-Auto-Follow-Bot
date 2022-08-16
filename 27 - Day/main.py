from tkinter import *


window = Tk()
window.title("My First GUI App")
window.minsize(width=600, height=300)

# label component
my_label = Label(text="My First Label", font=("Arial", 20, "bold"))
# my_label.pack(side="left")
# my_label.pack(side="bottom")
# my_label.pack(expand=True)
my_label.pack()

# update label text
my_label["text"] = "new text"
my_label.config(text="hello")


#   Entry  ( INPUT FIELD )
entry = Entry()
entry.pack()


def entry_text():
    my_label.config(text=entry.get())


# button
def button_clicked():
    # print("Hello, Arunesh")
    # my_label["text"] = "Button Clicked"
    my_label.config(text="Button Clicked")


# button = Button(text="Click Me", command=button_clicked)
button = Button(text="Click Me", command=entry_text)
button.pack()























window.mainloop()
