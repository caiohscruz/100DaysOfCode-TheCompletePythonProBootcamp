from turtle import *
import colorgram
import random

# TODO 1: Extract color from an image


def extract_colors(file, num_colors):
    extraction = colorgram.extract(file, num_colors)
    colors = []
    for color in extraction:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        colors.append((red, green, blue))
    return colors


palette = extract_colors(file='colorful-photography.jpg', num_colors=10)

# TODO 2: Challenge square of dots


def random_color(colors):
    return random.choice(colors)


bob = Turtle()
screen = Screen()
colormode(255)

NUM_DOTS_PER_SIDE = 10
DOT_SIZE = 20
DOT_STEP = 50

bob.penup()
bob.hideturtle()

for _ in range(NUM_DOTS_PER_SIDE):
    bob.speed("fast")
    for _ in range(NUM_DOTS_PER_SIDE):
        bob_color = random_color(palette)
        bob.dot(DOT_SIZE, bob_color)
        bob.forward(DOT_STEP)
    bob.speed("fastest")
    bob.left(90)
    bob.forward(DOT_STEP)
    bob.right(90)
    bob.backward(DOT_STEP * NUM_DOTS_PER_SIDE)


screen.exitonclick()





