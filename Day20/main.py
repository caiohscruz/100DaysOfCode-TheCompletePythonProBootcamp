from turtle import Screen
from Snake import Snake



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(screen)
snake.movement()

def move_up():
    snake.heads_up()

screen.onkey(key='Up', fun=move_up)
screen.onkey(key='right', fun=snake.heads_right)
screen.onkey(key='down', fun=snake.heads_down)
screen.onkey(key='left', fun=snake.heads_left)
screen.listen()

screen.exitonclick()
