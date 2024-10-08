import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_car(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setposition(300, 20*random.randint(-12, 11)+10)
        car.setheading(180)
        self.cars.append(car)

    def move_car(self, car):
        car.forward(self.move_distance)

    def next_level(self):
        self.move_distance += MOVE_INCREMENT


