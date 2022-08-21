from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#   Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    new_password = "".join(password_list)

    print(f"Your password is: {new_password}")

    # clear password in input field
    password_entry.delete(0, END)

    # insert new password
    password_entry.insert(0, new_password)

    # copy password
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    #   store data in variables
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        return messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        #   UPDATE WITH NEW DATA
        try:
            with open("data.json", mode="r") as file_data:
                # reading json data
                data = json.load(file_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as file_data:
                json.dump(new_data, file_data, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", mode="w") as file_data:
                json.dump(new_data, file_data, indent=4)
        else:
            # updating json data
            data.update(new_data)
            with open("data.json", mode="w") as file_data:
                #   writing json file data with old and new data
                json.dump(data, file_data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="W")

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")


website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

email_entry = Entry(width=35)
email_entry.insert(0, "example@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")


generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2)


add_btn = Button(text="Add", command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")









































window.mainloop()
