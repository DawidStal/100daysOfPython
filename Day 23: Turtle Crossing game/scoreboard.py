from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.setposition(-285, 250)
        self.write(f"Level {self.level}", align="left", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
