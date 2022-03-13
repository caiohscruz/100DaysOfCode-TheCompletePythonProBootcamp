import tkinter

window = tkinter.Tk()

window.title("Mile to Km Converter")

window.config(padx=20, pady=20)

FONT = ("Arial", 12, "normal")

input_miles = tkinter.Entry(width=10)
lbl_miles = tkinter.Label(text="Miles", font=FONT)
lbl_kilometers = tkinter.Label(text="Km", font=FONT)
lbl_text = tkinter.Label(text="is equal to", font=FONT)
lbl_result = tkinter.Label(text="0", font=FONT)

input_miles.grid(column=1, row=0)
lbl_miles.grid(column=2, row=0)
lbl_text.grid(column=0, row=1)
lbl_result.grid(column=1, row=1)
lbl_kilometers.grid(column=2, row=1)


def convert_miles_to_kilometers():
    kilometers = float(input_miles.get()) * 1.60934
    lbl_result.config(text=round(kilometers, 3))


btn_converter = tkinter.Button(text="Calculate", command=convert_miles_to_kilometers)
btn_converter.grid(column=1, row=3)

window.mainloop()
