from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()

# TODO 1: Make a square
# for _ in range(4):
#     bob.forward(100)
#     bob.right(90)

# TODO 2: Draw a Dashed Line
for _ in range(15):
    bob.forward(10)
    bob.penup()
    bob.forward(10)
    bob.pendown()

screen.exitonclick()