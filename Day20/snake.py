import time
from turtle import Turtle

INITIAL_LENGTH = 3
SNAKE_COLOR = "white"

starting_positions = []
for i in range(INITIAL_LENGTH):
    x_axis = -20 * i
    y_axis = 0
    starting_positions.append((x_axis, y_axis))

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, initial_delay):
        self.body = []
        self.snake_length = 0
        self.delay = initial_delay
        for _ in range(INITIAL_LENGTH):
            self.get_bigger()
        self.head = self.body[0]
        self.set_initial_position()

    def get_bigger(self):
        self.body.append(self.create_part())
        self.snake_length += 1

    @staticmethod
    def create_part():
        part = Turtle(shape="square", visible=False)
        part.penup()
        part.speed("fastest")
        part.color(SNAKE_COLOR)
        return part

    def set_initial_position(self):
        for i in range(self.snake_length):
            self.body[i].goto(starting_positions[i])
            self.body[i].showturtle()

    def move(self):
        time.sleep(self.delay)
        old_position = self.head.pos()
        self.head.forward(20)
        self.move_body(self.body[1], old_position)

    def move_body(self, part, new_position):
        index = self.body.index(part)
        old_position = part.pos()
        part.goto(new_position)
        if not part.isvisible():
            part.showturtle()
        if index + 1 < self.snake_length:
            self.move_body(self.body[index+1], old_position)

    def heads_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def heads_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def heads_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def heads_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def accelerate(self):
        self.delay *= 0.95

    def eats(self):
        self.get_bigger()
        if self.snake_length < 26 and self.snake_length % 10 == 0:
            self.accelerate()