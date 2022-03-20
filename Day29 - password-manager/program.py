import tkinter as tk


# ------------------------------------------ PASSWORD GENERATOR ------------------------------------------ #

def generate_password():
    return True

# ------------------------------------------ SAVE PASSWORD ------------------------------------------ #


def save_password():
    return True;

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

input_id = tk.Entry(width=51)
input_id.grid(column=1, row=2, columnspan=2)

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