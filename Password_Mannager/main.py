"""
------------------------WHAT THIS PROGRAM DOES---------------------------------
Sometime you create account on lot of website with different password or email and it became hard for
you to remember them.

Well this application helps you to deal with such problem. It saves all your email and password of
different website. It also allow you to search through your database and see the information about
particular website.

"""
import pyperclip
import json
import random
import string
import tkinter as tk
from tkinter import END, messagebox

# ================================CONSTANT====================================

TITLE = 'Password Manager'
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 200
WINDOW_PADX = 50
WINDOW_PADY = 50
FONT_SIZE = 15
FONT_NAME = 'Arial'
FONT_WEIGHT = 'normal'
COMPONENTS_PADY = 5
DATABASE = 'data.json'


# ================================COPY====================================
def copy_to_clipboard(data_to_copy):
    """
    Copy the password that you entered in the password field
    """
    copy_text = data_to_copy.get()
    if copy_text:
        pyperclip.copy(copy_text)
        messagebox.showinfo(title='Clipboard', message='Copied successfully')
    else:
        messagebox.showerror(title='Clipboard', message='First enter something inside the field')


# ================================SEARCHING DATABASE====================================
def search_database():
    """
    Search the database for the information available for entered website.
    It will tell you no information is given if there is no record for entered website
    """
    website_data = website_entry.get().capitalize()
    if len(website_data) == 0:
        messagebox.showerror(title='Error', message='Type website name to search in database')
        return
    try:
        with open(DATABASE) as data_file:
            data = json.load(data_file)
            email_data = data[website_data]['email']
            password_data = data[website_data]['password']
    except (FileNotFoundError, KeyError):
        messagebox.showinfo(title='Message from database', message=f'No information exist about {website_data}')
    else:
        messagebox.showinfo(title='Website detail', message=f'Email and password for website {website_data}\n\n'
                                                            f'Email: {email_data}\n'
                                                            f'Password: {password_data}')


# ===============================PASSWORD GENERATOR=====================================
def generate_password():
    """
    This function generate random password for your use
    """

    # Contains all the letter both upper and lowercase
    letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    characters = ['!', '@', '#', '$', '%', '^', '&', '&', '*', '(', ')', '-', '<', '>']

    # We shuffled the data because we need them to not start from 0 always, They must be choosen random
    # ly
    random.shuffle(letters)
    random.shuffle(numbers)
    random.shuffle(characters)
    number_of_letters = random.randint(8, 10)
    number_of_numbers = random.randint(4, 6)
    number_of_character = random.randint(3, 5)

    letters = [letters[i] for i in range(number_of_letters)]
    numbers = [numbers[i] for i in range(number_of_numbers)]
    characters = [characters[i] for i in range(number_of_character)]

    password_list = letters + numbers + characters
    random.shuffle(password_list)
    generated_password = ''.join(password_list)

    # To delete the previous generated password (if any)
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)


# ===============================SAVE DATA=====================================
def save_to_file():
    """
    Save all the information that you have entered to your database
    """
    website_data = website_entry.get().capitalize()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if not all([len(website_data), len(email_data), len(password_data)]):
        messagebox.showerror(title='Error', message='Please fill all the required filed')
        return

    is_ok = messagebox.askokcancel(title='Confirmation', message=f'These are the field you entered\n\n'
                                                                 f'Website: {website_data}\n'
                                                                 f'Email: {email_data}\n'
                                                                 f'Password: {password_data}\n\n'
                                                                 f'If you are ok with this press ok')

    if is_ok:
        try:
            with open(DATABASE, 'r') as data:
                # Reading the data
                data_json = json.load(data)

        except FileNotFoundError:
            with open(DATABASE, 'w') as data:
                json.dump(new_data, data, indent=4)

        else:
            # Updating the data
            data_json.update(new_data)
            with open(DATABASE, 'w') as data:
                # Writing the overall data
                json.dump(data_json, data, indent=4)

        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ===============================UI SETUP=====================================
window = tk.Tk()
window.title(TITLE)
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(padx=WINDOW_PADX, pady=WINDOW_PADY)

# Creating canvas
canvas = tk.Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

# Using canvas we can't directly give the image location.
# First we need the read the given image
# and this is done using PhotoImage class in tkinter. This PhotoImage class take image location as an
# argument and return the image object which we can store in variable and use it wherever we want

logo = tk.PhotoImage(file='logo.png')
canvas.create_image(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, image=logo)

# ==================================CREATING COMPONENTS===========================================

# Creating Labels
website_name = tk.Label(text='Website: ', font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))
email = tk.Label(text='Email/Username: ', font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))
password = tk.Label(text='Password: ', font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))

# Creating Entry
website_entry = tk.Entry(width=25, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))
email_entry = tk.Entry(width=50, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))
password_entry = tk.Entry(width=25, font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT))

# Creating Button
generate_button = tk.Button(text='Generate Password', width=25, font=(FONT_NAME, FONT_SIZE - 5, FONT_WEIGHT),
                            command=generate_password)
add_button = tk.Button(text='Add', width=50, font=(FONT_NAME, FONT_SIZE - 5, FONT_WEIGHT),
                       command=save_to_file)
search_button = tk.Button(text='Search', width=25, font=(FONT_NAME, FONT_SIZE - 5, FONT_WEIGHT),
                          command=search_database)
copy_password_button = tk.Button(text='Copy password', width=25, font=(FONT_NAME, FONT_SIZE - 5, FONT_WEIGHT),
                                 command=lambda: copy_to_clipboard(password_entry))
copy_email_button = tk.Button(text='Copy email', width=25, font=(FONT_NAME, FONT_SIZE - 5, FONT_WEIGHT),
                              command=lambda: copy_to_clipboard(email_entry))

# ==================================POSITION===========================================

# defining position of canvas
canvas.grid(column=1, row=0, sticky='e')

# Defining position of all labels
website_name.grid(column=0, row=1)
email.grid(column=0, row=2)
password.grid(column=0, row=3)

# Defining position of all entry
website_entry.grid(column=1, row=1, sticky='ew', pady=COMPONENTS_PADY)
website_entry.focus()
email_entry.grid(column=1, row=2, columnspan=2, sticky='ew', pady=COMPONENTS_PADY)
password_entry.grid(column=1, row=3, sticky='ew', pady=COMPONENTS_PADY)

# Defining position of all button
generate_button.grid(column=2, row=3, sticky='e', pady=COMPONENTS_PADY)
add_button.grid(column=1, row=4, columnspan=2, sticky='ew', pady=COMPONENTS_PADY)
search_button.grid(column=2, row=1, sticky='e', pady=COMPONENTS_PADY)
copy_password_button.grid(column=1, row=5, sticky='w', pady=COMPONENTS_PADY + 10)
copy_email_button.grid(column=2, row=5, sticky='e', pady=COMPONENTS_PADY + 10)

window.mainloop()
