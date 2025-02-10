from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-200, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(200, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def score_update(self):
        self.clear()
        self.goto(-200, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(200, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def r_point(self):
        self.r_score += 1
        self.score_update()

    def l_point(self):
        self.l_score += 1
        self.score_update()
