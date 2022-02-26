from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# less delay is more speed
INITIAL_DELAY = 0.3

screen = Screen()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(INITIAL_DELAY)
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
scoreboard = ScoreBoard(SCREEN_HEIGHT)

screen.listen()
screen.onkeypress(snake.heads_up, "Up")
screen.onkeypress(snake.heads_right, "Right")
screen.onkeypress(snake.heads_down, "Down")
screen.onkeypress(snake.heads_left, "Left")

while True:
    screen.update()
    snake.move()
    if snake.head.distance(food) < 10:
        snake.eats()
        scoreboard.update_score()
        food.refresh_position()

screen.exitonclick()
