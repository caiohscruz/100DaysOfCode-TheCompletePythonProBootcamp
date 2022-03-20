import tkinter as tk
from tkinter import messagebox
import pandas as pd


# ------------------------------------------ PASSWORD GENERATOR ------------------------------------------ #

def generate_password():
    return True

# ------------------------------------------ SAVE PASSWORD ------------------------------------------ #


FILE_NAME = "pass.csv"


def save_password():
    data = pd.read_csv(FILE_NAME)

    website = input_website.get()
    identifier = input_id.get()
    password = input_password.get()

    if has_empty_input(website, identifier, password):
        messagebox.showwarning(title="Oooops", message="Please don't leave any fields empty!")
        return

    if register_exists(data, website, identifier):
        want_update = messagebox.askokcancel(title="Attention", message="Register already exists. Update?")
        if want_update:
            remove_previous_register(data, website, identifier)
        else:
            messagebox.showinfo(title="Attention", message="Changes not executed")
            return

    data = add_register(data, website, identifier, password)
    print(data)

    data.to_csv(FILE_NAME, index=False)

    messagebox.showinfo(title="Attention", message="Password was saved")

    input_website.delete(0, 'end')
    input_password.delete(0, 'end')


def has_empty_input(website, identifier, password):
    return (website == "") or (identifier == "") or (password == "")


def register_exists(df, website, identifier):
    search = df[(df['website'] == website) & (df['id'] == identifier)]
    return len(search) > 0


def remove_previous_register(df, website, identifier):
    df.drop(df.loc[(df['website'] == website) & (df['id'] == identifier)].index, inplace=True)


def add_register(df, website, identifier, password):
    register = pd.DataFrame({'website': [website], 'id': [identifier], 'password': [password]})
    return pd.concat([df, register])

# ------------------------------------------ UI SETUP ------------------------------------------ #


FONT = "Courier"

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

input_website = tk.Entry(width=51)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_id = tk.Entry(width=51)
input_id.grid(column=1, row=2, columnspan=2)
input_id.insert(0, "teste@teste.com")

input_password = tk.Entry(width=33)
input_password.grid(column=1, row=3)

lbl_website = tk.Label(text="Website:")
lbl_website.grid(column=0, row=1)

lbl_id = tk.Label(text="Email/Username:")
lbl_id.grid(column=0, row=2)

lbl_password = tk.Label(text="Password")
lbl_password.grid(column=0, row=3)

btn_generate_password = tk.Button(text="Generate Password", command=generate_password)
btn_generate_password.grid(column=2, row=3)

btn_add = tk.Button(text="Add", command=save_password, width=43)
btn_add.grid(column=1, row=4, columnspan=2)


window.mainloop()