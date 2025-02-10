from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.goto(20 * random.randint(-14, 14), 20 * random.randint(-14, 14))

    # Create new food at a random position
    def refresh(self):
        random_x = 20 * random.randint(-14,14)
        random_y = 20 * random.randint(-14,14)
        self.goto(random_x, random_y)

