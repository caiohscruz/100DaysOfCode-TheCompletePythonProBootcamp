from turtle import Turtle

INITIAL_STEP = 10
INITIAL_SPEED = 0.1

class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.step = INITIAL_STEP
        self.move_speed = INITIAL_SPEED

    def move(self):
        self.forward(self.step)

    def change_angle(self, angle):
        self.setheading(angle)

    def v_bounce(self):
        angle = self.heading()
        self.setheading(-angle)

    def h_bounce(self):
        angle = self.heading()
        self.setheading(180-angle)
        self.move_speed *= 0.9

    def back_to_center(self):
        self.goto(0, 0)
        self.move_speed = INITIAL_SPEED

    def speed_up(self):
        self.step += 0.1
