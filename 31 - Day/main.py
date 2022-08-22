from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"


#################################################################################################
#
#               READ CSV DATA
#
#################################################################################################
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)

    flip_timer = window.after(2000, flip_card)


#################################################################################################
#
#               UI
#
#################################################################################################

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(2000, flip_card)

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR, command=next_card)
right_btn.grid(row=1, column=1)


next_card()




































window.mainloop()
