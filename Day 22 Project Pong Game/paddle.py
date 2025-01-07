from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    # go up method
    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    # go down method
    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -250:
            self.goto(self.xcor(), new_y)
