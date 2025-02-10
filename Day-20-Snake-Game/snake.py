from turtle import Turtle

Starting_positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #Create a snake element in each starting position
    def create_snake(self):
        for position in Starting_positions:
            self.add_segment(position)

    # Add a new block segment to the snake body
    def add_segment(self, position):
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.setposition(position)
        self.segments.append(block)

    # Create a new segment at the postion of the last one
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Move the snake forward
    def move(self):
        for block_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[block_num-1].xcor()
            new_y = self.segments[block_num-1].ycor()
            self.segments[block_num].goto(new_x, new_y)
        self.head.forward(20)

    # Functions to change the snake heading by 90 degrees
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
