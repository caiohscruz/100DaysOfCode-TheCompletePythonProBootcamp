from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self, max_x_cor, max_y_cor):
        super().__init__()
        self.max_x_cor = max_x_cor
        self.max_y_cor = max_y_cor
        self.min_x_cor = - self.max_x_cor
        self.min_y_cor = - self.max_y_cor
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.color("red")
        self.refresh_position()

    def refresh_position(self):
        x_cor = random.randint(self.min_x_cor/20, self.max_x_cor/20) * 20
        y_cor = random.randint(self.min_y_cor/20, self.max_y_cor/20) * 20
        self.goto(x_cor, y_cor)
