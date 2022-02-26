from turtle import *
from NamedTurtle import NamedTurtle
import random


def draw_finish_line(x_cor, screen_height):
    pencil = Turtle()
    pencil.setheading(270)
    line_lenght = 0.9 * screen_height
    y_cor = line_lenght / 2
    pencil.penup()
    pencil.setpos(x_cor, y_cor)
    pencil.pendown()
    pencil.write("Finish Line", False, align="left")
    pencil.forward(line_lenght)


screen = Screen()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

names = ["donatello", "rafael", "leonardo", "michelangelo"]
colors = ["purple", "red", "blue", "orange"]
y_axis = [-120, -40, 40, 120]

num_turtles = len(names)
space_between = SCREEN_HEIGHT / (num_turtles + 1)

PROPORTION_ROAD_WIDTH = 0.7
RACE_DISTANCE = PROPORTION_ROAD_WIDTH * SCREEN_WIDTH

all_turtles = []

STARTING_POINT_XCOR = - SCREEN_WIDTH * PROPORTION_ROAD_WIDTH / 2

FINISH_LINE_XCOR = STARTING_POINT_XCOR + RACE_DISTANCE
draw_finish_line(FINISH_LINE_XCOR, SCREEN_HEIGHT)


for number in range(0, num_turtles):
    racer = NamedTurtle(color=colors[number], name=names[number])
    starting_point_ycor = - SCREEN_HEIGHT / 2 + (number + 1) * space_between
    racer.set_position(x=STARTING_POINT_XCOR, y=starting_point_ycor)
    racer.write_name()
    all_turtles.append(racer)

game_is_over = False

guess = ""
while guess not in names:
    guess = screen.textinput(title="Which turtle will win?", prompt="Your guess:").lower()

NUM_STEPS = 5

while not game_is_over:
    racer = random.choice(all_turtles)
    racer.turtle.forward(NUM_STEPS)
    if racer.turtle.xcor() >= FINISH_LINE_XCOR:
        game_is_over = True
        print(f"The winner was {racer.name}")
        if racer.name == guess:
            text = "You win!"
        else:
            text = "You lose!"
        racer.turtle.write(text, False, align="right")


screen.exitonclick()