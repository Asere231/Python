from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH PASSWORD ---------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("data.json", mode="r") as data:
            data_file = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="NO DATA FILE FOUND.")
    else:
        if website in data_file:
            email = data_file[website]["email"]
            found_password = data_file[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {found_password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list).lower()
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_data():
    website = web_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data:
                # Reading old data
                data_file = json.load(data)

        except FileNotFoundError:
            with open("data.json", mode="w") as data:
                json.dump(new_data, data, indent=4)

        else:
            # Updating old data with new data
            data_file.update(new_data)

            with open("data.json", mode="w") as data:
                # Saving updated data
                json.dump(data_file, data, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# --------- LABELS ---------- #
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# --------- ENTRIES ---------- #
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "bryan@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# --------- BUTTONS ---------- #
generate_button = Button(text="Generate Password", width=11, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=store_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
