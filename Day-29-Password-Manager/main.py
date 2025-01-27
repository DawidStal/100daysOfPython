from tkinter import *
from tkinter import messagebox
import json
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)


# ---------------------------- SEARCH WEBSITE ------------------------------ #
def search():
    website = website_input.get()
    try:
        with open("Day-29-Password-Manager\\data.json", "r") as file:
            data = json.load(file)
        search_data = data[website]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found")
    except KeyError:
        messagebox.showerror(title="Error", message="Website not found")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Website not found")
    else:
        messagebox.showinfo(title=f"{website}", message=f"Email: {search_data["email"]} \nPassword: {search_data["password"]}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get info from entries
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:
        {
            "email": email,
            "password": password
        }
    }

    # Check for empty entries
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Entries Empty", message="Please don't leave any fields empty.")
    else:
        try:
            with open("Day-29-Password-Manager\\data.json", "r") as file:
                # read and update old data
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("Day-29-Password-Manager\\data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("Day-29-Password-Manager\\data.json", "w") as file:
                # save updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=30)

# Image
lockImage = PhotoImage(file="Day-29-Password-Manager\\logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lockImage)
canvas.grid(column=1, row=0)

# Website
website_text = Label(text="Website")
website_text.grid(column=0, row=1)
website_input = Entry()
website_input.focus()
website_input.grid(column=1, row=1, sticky="EW")

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="EW")

# Email
email_text = Label(text="Email/Username")
email_text.grid(column=0, row=2)
email_input = Entry()
email_input.insert(0, "")
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")

# Password
password_text = Label(text="Password")
password_text.grid(column=0, row=3)
password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

generate_password = Button(text="Generate Password", command=generate)
generate_password.grid(column=2, row=3, sticky="EW")

# Add details
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
