import tkinter

window = tkinter.Tk()

window.title("Working with GUI in Python")

window.minsize(width=500, height=300)

window.config(padx=20, pady=20)


my_label = tkinter.Label(text="test", font=("Arial", 24, "normal"))
# my_label.pack()
my_label.grid(column=0, row=0)
my_label.config(padx=30, pady=20)


w_input = tkinter.Entry(width=10)
# w_input.pack()
w_input.grid(column=3, row=2)


def button_click():
    text = w_input.get()
    my_label.config(text=text)


btn = tkinter.Button(text="Click me", command=button_click)
# btn.pack()
btn.grid(column=1, row=1)

new_btn = tkinter.Button(text="Click me²", command=button_click)
new_btn.grid(column=2, row=0)


window.mainloop()
