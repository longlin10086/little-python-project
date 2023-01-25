from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_data():
    web = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        web:{
            "email": email,
            "password": password,
        }
    }
    if web == '' or password == '' or email == '':
            messagebox.showinfo(title="Waring", message="Please don't leave any fields empty!")
    elif is_ok := messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email}\n" 
                                                            f"Password: {password}\nIs it ok to save?"):
        try:
            with open("/personal_info/password.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("/personal_info/password.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("/personal_info/password.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web = website_entry.get().title()
    try:
        with open("/personal_info/password.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        try:
            messagebox.showinfo(title=web, message=f"email:{data[web]['email']}\n"
                                               f"password:{data[web]['password']}")
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.insert(END, data[web]['password'])
            email_entry.insert(END, data[web]['email'])
            pyperclip.copy(data[web]['password'])
        except KeyError:
            messagebox.showinfo(title="Error", message="No details for the website exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='white')


canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
photo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg='white')
website_label.grid(column=0, row=1)


email_label = Label(text="Email/Username:", bg='white')
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg='white')
password_label.grid(column=0, row=3)

website_entry = Entry(width=36)
website_entry.grid(column=1, columnspan=2, row=1, sticky="w")
website_entry.focus()

email_entry = Entry(width=36)
email_entry.insert(0, "longlin@email.com")
email_entry.grid(column=1, columnspan=2, row=2, sticky="w")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

password_button = Button(text="Generate Password", width=15, bg='white', command=generate_password)
password_button.grid(column=1, row=3, columnspan=2, sticky="e")

add_button = Button(text="Add", width=36, bg='white', command=add_to_data)
add_button.grid(column=1, columnspan=2, row=4, sticky="w")

search_button = Button(text="Search", width=15, bg="white", command=find_password)
search_button.grid(column=1, columnspan=2, row=1, sticky="e")

window.mainloop()
