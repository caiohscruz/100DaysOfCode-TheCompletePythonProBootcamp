from turtle import *

bob = Turtle()
screen = Screen()


def move_forwards():
    bob.forward(2)


def move_backwards():
    bob.backward(2)


def move_counter_clockwise():
    bob.left(2)


def move_clockwise():
    bob.right(2)


def reset_screen():
    bob.reset()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=move_counter_clockwise)
screen.onkeypress(key="d", fun=move_clockwise)
screen.onkeypress(key="c", fun=reset_screen)

screen.exitonclick()