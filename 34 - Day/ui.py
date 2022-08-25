from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Quiz Text", font=("Arial", 16, "italic"))
        self.canvas.config(bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, font=("Arial", 12, "normal"), fg="white")
        self.score_label.grid(column=1, row=0)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, bd=0)
        self.true_button.grid(column=0, row=2)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, bd=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
