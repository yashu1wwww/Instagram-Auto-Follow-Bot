from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"
# FONT = ("Arial", )


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_image)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR)
wrong_btn.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR)
right_btn.grid(row=1, column=1)







































window.mainloop()
