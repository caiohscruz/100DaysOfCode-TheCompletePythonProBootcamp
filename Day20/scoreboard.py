from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 14, 'normal')


class ScoreBoard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        top = screen_height / 2 - 20
        self.goto(x=0, y=top)
        self.score = -1
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT, move=False)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT, move=False)
