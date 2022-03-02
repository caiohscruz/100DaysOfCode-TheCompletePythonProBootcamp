import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = HEIGHT

MAX_Y = HEIGHT * 0.40
MIN_Y = - MAX_Y

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard(HEIGHT, WIDTH)
car_manager = CarManager(range_y=(MIN_Y, MAX_Y), screen_width=WIDTH)

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
iteration = 0


def level_up():
    scoreboard.update_score()
    car_manager.accelerate()


def detect_collision():
    for car in car_manager.all_cars:
        if not car.is_new:
            if abs(car.ycor() - player.ycor()) < 20:
                return abs(car.xcor() - player.xcor()) < 25
    return False


while game_is_on:
    time.sleep(0.05)
    screen.update()
    iteration += 1
    if iteration % 6 == 0:
        car_manager.create_car()
    car_manager.move()

    if detect_collision():
        scoreboard.game_over()
        game_is_on = False

    if player.ycor() > MAX_Y + 20:
        level_up()
        player.go_to_start()

screen.exitonclick()