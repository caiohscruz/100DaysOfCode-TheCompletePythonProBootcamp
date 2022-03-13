import tkinter

window = tkinter.Tk()

window.title("Working with GUI in Python")

window.minsize(width=500, height=300)


my_label = tkinter.Label(text="test", font=("Arial", 24, "normal"))
my_label.pack()

w_input = tkinter.Entry(width=10)
w_input.pack()


def button_click():
    text = w_input.get()
    my_label.config(text=text)


btn = tkinter.Button(text="Click me", command=button_click)
btn.pack()



window.mainloop()
