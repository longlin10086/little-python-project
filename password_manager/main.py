from tkinter import *
from tkinter import messagebox
import random
import pyperclip
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
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    text = [web, email, password]
    if web == '' or password == '' or email == '':
            messagebox.showinfo(title="Waring", message="Please don't leave any fields empty!")
    elif is_ok := messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email}\n" 
                                                            f"Password: {password}\nIs it ok to save?"):
        with open("data.txt", "a") as data:
            data.write(" | ".join(text))
            data.write("\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
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
website_label.focus()

email_label = Label(text="Email/Username:", bg='white')
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg='white')
password_label.grid(column=0, row=3)

website_entry = Entry(width=36)
website_entry.grid(column=1, columnspan=2, row=1, sticky="w")

email_entry = Entry(width=36)
email_entry.insert(0, "longlin@email.com")
email_entry.grid(column=1, columnspan=2, row=2, sticky="w")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

password_button = Button(text="Generate Password", width=15, bg='white', command=generate_password)
password_button.grid(column=1, row=3, columnspan=2, sticky="e")

add_button = Button(text="Add", width=36, bg='white', command=add_to_data)
add_button.grid(column=1, columnspan=2, row=4, sticky="w")

window.mainloop()
