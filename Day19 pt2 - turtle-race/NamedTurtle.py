from turtle import *


class NamedTurtle:

    def __init__(self, color, name):
        self.turtle = Turtle()
        self.name = name
        self.turtle.color(color)
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.position = 0

