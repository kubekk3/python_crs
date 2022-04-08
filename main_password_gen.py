from email.mime import image
import tkinter as tk
from turtle import title
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [random.choice(letters) for letter in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for number in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for symbol in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_input.delete(0, tk.END)
    pass_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_name.get()
    email = email_name.get()
    password = pass_input.get()
    if len(website) >0  and len(email) >0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are your details entered:\n Email: {email}, Password: {password} \nContinue or cancel")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                web_input.delete(0, tk.END)
                pass_input.delete(0, tk.END)
    else:
        messagebox.showerror(title="Error", message="Fill every field!")

# ---------------------------- UI SETUP ------------------------------- #
#WINDOW
window = tk.Tk()
window.title("Password menager")
window.config(padx=50, pady=50)

#CANVAS
canvas = tk.Canvas(width=200,height=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(column=1, row=0)

#WEBSITE LABEL
web_label = tk.Label()
web_label.config(text="Website")
web_label.grid(column=0, row=1)

#WEBSITE INPUT
website_name = tk.StringVar()
web_input = tk.Entry(window, textvariable=website_name, width=45)
web_input.grid(column=1, row=1, columnspan=2)


#EMAIL LABEL
email_label = tk.Label()
email_label.config(text="Email/Username")
email_label.grid(column=0, row=2)

#EMAIL INPUT
email_name = tk.StringVar()
email_input = tk.Entry(window, textvariable=email_name, width=45)
email_input.grid(column=1, row=2, columnspan=2)

#PASSWORD LABEL
pass_label = tk.Label()
pass_label.config(text="Password")
pass_label.grid(column=0, row=3)

#PASSWORD INPUT
pass_name = tk.StringVar()
pass_input = tk.Entry(window, textvariable=pass_name, width=35)
pass_input.grid(column=1, row=3)

#GENERATE BUTTON
gen_button = tk.Button()
gen_button.config(text="Generate", command=generate_password)
gen_button.grid(column=2, row=3, columnspan=2)

#ADD BUTTON
add_button = tk.Button()
add_button.config(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()