from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- #


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Promodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


#   labels
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(text="✔", fg=GREEN, font=(FONT_NAME, 15, "normal"), bg=YELLOW)
check_label.grid(column=1, row=3)

#   buttons
start_button = Button(text="Start", highlightthickness=0, borderwidth=1)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, borderwidth=1)
reset_button.grid(column=2, row=2)


window.mainloop()
