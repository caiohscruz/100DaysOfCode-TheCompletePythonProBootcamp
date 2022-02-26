from turtle import Screen
from Snake import Snake

# less delay is more speed
INITIAL_DELAY = 0.5

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(INITIAL_DELAY)

screen.listen()
screen.onkeypress(snake.heads_up, "Up")
screen.onkeypress(snake.heads_right, "Right")
screen.onkeypress(snake.heads_down, "Down")
screen.onkeypress(snake.heads_left, "Left")

while True:
    screen.update()
    snake.move()

screen.exitonclick()
