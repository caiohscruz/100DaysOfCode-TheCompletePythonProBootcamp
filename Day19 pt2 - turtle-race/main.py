from turtle import *
from NamedTurtle import NamedTurtle
import random

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

x_axis = - SCREEN_WIDTH * PROPORTION_ROAD_WIDTH / 2

for number in range(0, num_turtles):
    racer = NamedTurtle(color=colors[number], name=names[number])
    y_axis = - SCREEN_HEIGHT / 2 + (number + 1) * space_between
    racer.turtle.setpos(x_axis, y_axis)
    racer.turtle.write(racer.name, False, align="right")
    all_turtles.append(racer)

game_is_over = False

guess = ""
while guess not in names:
    guess = screen.textinput(title="Which turtle will win?", prompt="Your guess:").lower()

NUM_STEPS = 5

while not game_is_over:
    racer = random.choice(all_turtles)
    racer.turtle.forward(NUM_STEPS)
    if racer.turtle.xcor() >= RACE_DISTANCE + x_axis:
        game_is_over = True
        print(f"The winner was {racer.name}")
        if racer.name == guess:
            text = "You win!"
        else:
            text = "You lose!"
        racer.turtle.write(text, False, align="right")


screen.exitonclick()