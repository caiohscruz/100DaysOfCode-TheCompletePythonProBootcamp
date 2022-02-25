import time
from turtle import Turtle

INITIAL_LENGTH = 3
SNAKE_COLOR = "white"

starting_positions = []
for i in range(INITIAL_LENGTH):
    x_axis = -20 * i
    y_axis = 0
    starting_positions.append((x_axis, y_axis))

# less delay is more speed
INITIAL_DELAY = 0.5

class Snake:

    def __init__(self, screen):
        self.screen = screen
        self.body = []
        self.snake_length = 0
        self.delay = INITIAL_DELAY
        for _ in range(INITIAL_LENGTH):
            self.get_bigger()
        self.set_initial_position()

    def get_bigger(self):
        self.body.append(self.create_part())
        self.snake_length += 1

    @staticmethod
    def create_part():
        part = Turtle(shape="square")
        part.penup()
        part.color(SNAKE_COLOR)
        return part

    def set_initial_position(self):
        for i in range(self.snake_length):
            self.body[i].goto(starting_positions[i])

    def move_head(self):
        head = self.body[0]
        head_position = head.pos()
        head.forward(20)
        self.move_body(self.body[1], head_position)

    def move_body(self, part, new_position):
        index = self.body.index(part)
        part_position = part.pos()
        part.goto(new_position)
        if index + 1 < self.snake_length:
            self.move_body(self.body[index+1], part_position)

    def movement(self):
        while True:
            self.screen.update()
            time.sleep(self.delay)
            self.body[0].left(90)
            self.move_head()

    def heads_up(self):
        self.body[0].setheading(90)

    def heads_down(self):
        self.body[0].setheading(270)

    def heads_right(self):
        self.body[0].setheading(0)

    def heads_left(self):
        self.body[0].setheading(180)