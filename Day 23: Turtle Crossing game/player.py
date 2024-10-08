from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.setposition(0, -280)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.setposition(0, -280)

    def check_collision(self, car):
        if 10 >= self.ycor() - car.ycor() >= -10 and 30 >= car.xcor() > -30:
            return True

