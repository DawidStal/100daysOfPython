from turtle import Turtle


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def name_state(self, state, x, y):
        self.goto(x, y)
        self.write(state, font=("Arial", 8, "normal"))
