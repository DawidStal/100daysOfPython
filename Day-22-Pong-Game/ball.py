from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        self.x_dir = random.choice([-1, 1])
        self.y_dir = random.choice([-1, 1])
        self.move_speed = 0.005
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(random.randint(0, 360))

    def move_ball(self):
        self.setposition(self.xcor() + self.x_dir, self.ycor() + self.y_dir)

    def bounce_y(self):
        self.move_speed *= 0.9
        self.y_dir *= -1

    def bounce_x(self):
        self.x_dir *= -1

    def reset(self):
        self.move_speed = 0.005
        self.goto(0,0)
        self.bounce_x()


