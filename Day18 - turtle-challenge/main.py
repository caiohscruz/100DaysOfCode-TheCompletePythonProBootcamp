from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()

# TODO 1: Make a square
# for _ in range(4):
#     bob.forward(100)
#     bob.right(90)

# TODO 2: Draw a Dashed Line
# for _ in range(15):
#     bob.forward(10)
#     bob.penup()
#     bob.forward(10)
#     bob.pendown()

# TODO 3: Draw polygons
import random


def change_color():
    red = random.random()
    blue = random.random()
    green = random.random()

    bob.color(red, green, blue)

def draw_shape(num_sides):
    angle = 360 / num_sides
    change_color()
    for _ in range(num_sides):
        bob.forward(100)
        bob.right(angle)


for num_sides in range(3, 13):
    draw_shape(num_sides)


screen.exitonclick()