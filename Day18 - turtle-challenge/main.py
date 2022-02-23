from turtle import *
import random

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
colormode(255)

def change_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    bob.color((red, green, blue))

def draw_shape(num_sides):
    angle = 360 / num_sides
    change_color()
    for _ in range(num_sides):
        bob.forward(100)
        bob.right(angle)

# for num_sides in range(3, 13):
#     draw_shape(num_sides)

# TODO 4: Generate a random walk
bob.pensize(10)
bob.speed("fastest")

directions = [0, 90, 180, 270]

num_steps = 100
for _ in range(num_steps):
    change_color()
    bob.forward(20)
    bob.setheading(random.choice(directions))


screen.exitonclick()