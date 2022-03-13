from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 10, 'normal')


class Pointer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_at(self, data, x_cor, y_cor):
        self.goto(x_cor, y_cor)
        self.write(f"{data}", align=ALIGNMENT, font=FONT, move=False)