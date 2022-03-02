from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')


class ScoreBoard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        top = screen_height / 2 - 150
        self.penup()
        self.goto(x=0, y=top)
        self.l_score = -1
        self.r_score = -1
        self.total_points = 0
        self.hideturtle()
        self.color("white")
        self.update_l_score()
        self.update_r_score()

    def update_score(self):
        self.clear()
        self.goto(-100, self.ycor())
        self.write(self.l_score, align=ALIGNMENT, font=FONT, move=False)
        self.goto(100, self.ycor())
        self.write(self.r_score, align=ALIGNMENT, font=FONT, move=False)

    def update_l_score(self):
        self.l_score += 1
        self.total_points += 1
        self.update_score()

    def update_r_score(self):
        self.r_score += 1
        self.total_points += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT, move=False)
