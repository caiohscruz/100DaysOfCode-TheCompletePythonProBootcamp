from turtle import Turtle

STEP = 20


class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x_position, y=0)

    def move(self, distance):
        new_y = self.ycor() + distance
        self.goto(x=self.xcor(), y=new_y)

    def go_up(self):
        self.move(STEP)

    def go_down(self):
        self.move(-STEP)