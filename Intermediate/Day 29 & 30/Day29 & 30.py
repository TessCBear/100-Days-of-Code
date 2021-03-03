from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Arial", 12, "normal")

# Functionality

def save():
    website_data = website_input.get()
    username_data = username_input.get()
    password_data = password_input.get()

    new_data = {
        website_data : {
            "username" : username_data,
            "password" : password_data,
        }
    }

    if len(website_data) == 0 or len(password_data) == 0 or len(username_data) == 0:
        messagebox.showwarning(title = "Invalid", message = "Missing information")
        
    else:

        okay = messagebox.askokcancel(title = website_data, message=f"Add these details? \nUsername: {username_data} \nPassword: {password_data}")

        if okay:
            try:
                with open(".\Intermediate\Day 29 & 30\\passwords.json", mode = "r") as passwords:
                    data = json.load(passwords)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data

            finally: 
                with open(".\Intermediate\Day 29 & 30\\passwords.json", mode = "w") as passwords:
                    json.dump(data, passwords, indent = 4)
            
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')

def find_password():
    try:
        with open(".\Intermediate\Day 29 & 30\\passwords.json") as passwords:
            data = json.load(passwords)
            username = data[website_input.get()]["username"]
            password = data[website_input.get()]["password"]

    except FileNotFoundError:
        messagebox.showwarning(title="File Not Found", message="You have not saved any passwords yet.")
    
    except KeyError:
        messagebox.showwarning(title="Website Not Found", message = "You have not saved a password for that site.")

    else:
            messagebox.showinfo(title = website_input.get(), message = f"Username: {username} \nPassword: {password}")

    finally:
        website_input.delete(0, 'end')
# Password generator
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_list_letters = [random.choice(letters) for char in range(nr_letters)]
    password_list_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_list_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_list_letters + password_list_numbers + password_list_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# UI
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width = 200, height = 200)
photo = PhotoImage(file = ".\Intermediate\Day 29 & 30\\logo.png")
canvas.create_image(100, 100, image = photo)
canvas.grid(column = 1, row = 0)

website = Label(text = "Website:", font = FONT)
website.grid(column = 0, row = 1)

username = Label(text = "Username:", font = FONT)
username.grid(column = 0, row =2)

password = Label(text = "Password:", font = FONT)
password.grid(column = 0, row = 3)

website_input = Entry(width = 35)
website_input.grid(column = 1, row = 1)
website_input.focus()

username_input = Entry(width = 54)
username_input.grid(column = 1, row = 2, columnspan = 2)
username_input.insert(0, "default username")

password_input = Entry(width = 35)
password_input.grid(column = 1, row = 3)

generate_password = Button(text = "Generate Password", command = password_gen)
generate_password.grid(column = 2, row = 3)

add_button = Button(text = "Add", width = 46, command = save)
add_button.grid(column = 1, row = 4, columnspan = 2)

search = Button(text = "Search", width = 15, command = find_password)
search.grid(column = 2, row = 1)


window.mainloop()