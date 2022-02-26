from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# less delay is more speed
INITIAL_DELAY = 0.3

screen = Screen()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

MAX_X_COR = SCREEN_WIDTH / 2 - 40
MAX_Y_COR = SCREEN_HEIGHT / 2 - 40

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(INITIAL_DELAY)
food = Food(MAX_X_COR, MAX_Y_COR)
scoreboard = ScoreBoard(SCREEN_HEIGHT)

screen.listen()
screen.onkeypress(snake.heads_up, "Up")
screen.onkeypress(snake.heads_right, "Right")
screen.onkeypress(snake.heads_down, "Down")
screen.onkeypress(snake.heads_left, "Left")


def draw_borders():
    pencil = Turtle()
    pencil.penup()
    pencil.hideturtle()
    pencil.color("white")
    pencil.goto((MAX_X_COR + 10), (MAX_Y_COR + 10))
    pencil.pendown()
    pencil.goto((MAX_X_COR + 10), - (MAX_Y_COR + 10))
    pencil.goto(-(MAX_X_COR + 10), - (MAX_Y_COR + 10))
    pencil.goto(- (MAX_X_COR + 10), (MAX_Y_COR + 10))
    pencil.goto(MAX_X_COR + 10, MAX_Y_COR + 10)


def is_out(head):
    # horizontal
    if head.xcor() ** 2 > MAX_X_COR ** 2:
        return True
    if head.ycor() ** 2 > MAX_Y_COR ** 2:
        return True
    return False


is_game_over = False

draw_borders()

while not is_game_over:
    screen.update()
    snake.move()
    if snake.head.distance(food) < 10:
        snake.eats()
        scoreboard.update_score()
        food.refresh_position()
    if is_out(snake.head):
        scoreboard.game_over()
        is_game_over = True


screen.exitonclick()
