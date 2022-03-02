import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import random

WIDTH = 800
HEIGHT = 600

PADDLE_X_POS = 350

DIRECTIONS = (45, 135, 225, 315)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle(-PADDLE_X_POS)
right_paddle = Paddle(PADDLE_X_POS)
ball = Ball()
scoreboard = ScoreBoard(HEIGHT)

screen.listen()
screen.onkeypress(key="w", fun=left_paddle.go_up)
screen.onkeypress(key="s", fun=left_paddle.go_down)
screen.onkeypress(key="Up", fun=right_paddle.go_up)
screen.onkeypress(key="Down", fun=right_paddle.go_down)

is_game_over = False


def collision_borders(ball, height):
    return abs(ball.ycor()) >= height / 2 - 10


def is_goal(ball):
    if abs(ball.xcor()) > PADDLE_X_POS:
        return True
    else:
        return False


def collision_paddle(ball, left_paddle, right_paddle):
    if abs(ball.xcor()) >= PADDLE_X_POS - 20:
        if ball.distance(left_paddle) <= 50 or ball.distance(right_paddle) <= 50:
            return True
    return False


while not is_game_over:
    ball.change_angle(random.choice(DIRECTIONS))
    round_is_on = True
    while round_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        if collision_paddle(ball, left_paddle, right_paddle):
            ball.h_bounce()
        elif collision_borders(ball, HEIGHT):
            ball.v_bounce()
        elif is_goal(ball):
            if ball.xcor() > 0:
                scoreboard.update_l_score()
            else:
                scoreboard.update_r_score()
            round_is_on = False
            ball.back_to_center()





screen.exitonclick()