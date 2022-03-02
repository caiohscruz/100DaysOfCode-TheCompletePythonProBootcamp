from turtle import Turtle

ALIGNMENT = 'left'
FONT = ('Courier', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self, screen_height, screen_width):
        super().__init__()
        y_pos = screen_height / 2 - 20
        x_pos = - screen_width / 2 + 20
        self.penup()
        self.goto(x=x_pos, y=y_pos)
        self.score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT, move=False)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT, move=False)
