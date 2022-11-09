# import all classes from tkinter
from tkinter import *
# messagebox is not a class but a module
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password generator: saves websites, generate passwords, add it to database and search through it

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # list comprehension where we pick a random letter from letters between 8-10 times
    password_letters = [choice(letters) for char in range(randint(8, 10))]
    # list comprehension for symbols
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    # list comprehension for numbers
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # join method characters in list and puts them into a string called password
    password = "".join(password_list)
    # auto-populates newly created password in password entry after it's created
    password_input.insert(0, f"{password}")
    # copies password
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            # loading/reading our old data_file as data, data is a dictionary
            data = json.load(data_file)
    # exception to catch searching for a file that doesn't exist
    except FileNotFoundError:
        # message telling user data file doesn't exist
        messagebox.showinfo(title="Error", message="File was not found.")
    else:
        # if website is in the dictionary, retrieve email and password
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            # displays email and password in a message
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No information related to {website} if found in the data file")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # gets hold of website entry text
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    # creating a nested dictionary containing information put into the website
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Checks input fields haven't been left empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure you haven't left any fields empty!")
    else:
        # Opening in read mode could cause file not found error
        try:
            with open("data.json", "r") as data_file:
                # load method reads json data into python dictionary
                # loading/reading our old data_file as data
                data = json.load(data_file)
        # File not found exception if file doesn't open
        # JSON exception useful for catching errors with blank json file
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # creating new data.json file
            with open("data.json", "w") as data_file:
                # saving updated data, when user clicks add, into data.json file overwriting previous data
                json.dump(new_data, data_file, indent=4)
        # Only executes if everything inside try block was successful
        else:
            # update old data with new_data,
            # it doesn't just append but adds it to the dictionary
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data into data.json file overwriting previous data
                json.dump(data, data_file, indent=4)
        finally:
            # deleting text entered by user in input boxes after written to file
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

# padding
window.config(padx=20, pady=20)
# creating canvas
canvas = Canvas(width=200, height=200)
# create image using PhotoImage class
MyPass_Image = PhotoImage(file="logo.png")
# create image inside the canvas, first two #'s are x & y coord.
canvas.create_image(100, 100, image=MyPass_Image)
# layout dimension
canvas.grid(column=1, row=0)

# Website, email, password labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Input Boxes, the sticky "sticks" the widget to the edges of the column
website_input = Entry()
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
# places cursor in textbox
website_input.focus()

email_input = Entry()
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
# pre populates text
email_input.insert(0, "shelomo@att.net")

password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

# Password, Add, and Search button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35,command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

# updates UI
window.mainloop()