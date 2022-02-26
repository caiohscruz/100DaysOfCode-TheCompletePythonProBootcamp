from turtle import *


class NamedTurtle:

    def __init__(self, color, name):
        self.turtle = Turtle()
        self.name = name
        self.turtle.color(color)
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.position = 0

    def set_position(self, x, y):
        self.turtle.setpos(x, y)

    def write_name(self):
        self.turtle.write(self.name, False, align="right")