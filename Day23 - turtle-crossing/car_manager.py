from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self, range_y, screen_width):
        self.all_cars = []
        self.step = STARTING_MOVE_DISTANCE
        self.x_pos = screen_width / 2 + 60
        self.y_min = range_y[0]
        self.y_max = range_y[1]

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.step = self.step
        x_pos = self.x_pos
        y_pos = random.randint(self.y_min, self.y_max)
        new_car.goto(x=x_pos, y=y_pos)
        new_car.setheading(180)
        new_car.is_new = True
        self.all_cars.append(new_car)

    def accelerate(self):
        self.step += MOVE_INCREMENT

    def move(self):
        for car in self.all_cars:
            if car.xcor() < - self.x_pos:
                self.all_cars.remove(car)
            else:
                car.forward(self.step)
                car.is_new = False
