from tkinter import *
from tkinter import messagebox
import random
import csv
import pyperclip


import os

csv_file_path = "data.csv"

if not os.path.exists(csv_file_path):
    with open(csv_file_path, 'w', newline='') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(["Website", "Email", "Password"])

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []
  password_list.extend(random.choice(letters) for char in range(nr_letters))
  password_list.extend(random.choice(symbols) for char in range(nr_symbols))
  password_list.extend(random.choice(numbers) for char in range(nr_numbers))

  random.shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def is_mail(email):
    at = False
    point = False
    for letter in email:
        if letter == '@':
            at = True
        elif letter == '.':
            point = True

    if at and point:
      return True
    return False
        


def save():
    website = website_entry.get()
    email = mail_entry.get()
    password = password_entry.get()

    is_ok = False

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
      messagebox.showinfo(title='Oops..', message="Please make sure you haven't left any fields empyt")

    elif not is_mail(email):
      messagebox.showinfo(title='Error', message="Invalid mail")
    else:
        is_ok = messagebox.askokcancel(
            title='Confirmation',
            message=(
                f"DETAILS ENTERED:\n\n"
                f"Website:\n {website}\n\n"
                f"Email:\n    {email}\n\n"
                f"Password:\n  {password}\n\n"
                "Is it ok to SAVE?"
            )
        )

        if is_ok:
            with open("data.csv", 'a', newline='') as data_file:
                writer = csv.writer(data_file)
                writer.writerow([website, email, password])
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

mail_label = Label(text='Email:')
mail_label.grid(row=2, column=0)
mail_entry = Entry(width=35)
mail_entry.insert(0, "chrstphr.chevalier@gmail.com")
mail_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

generate_pw_button = Button(text='Create Password', width=9, command=generate_password)
generate_pw_button.grid(row=3, column=2)

add_button = Button(text='Add', width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
