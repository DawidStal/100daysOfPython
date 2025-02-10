import turtle as t
import random
import colorgram

colors = colorgram.extract('Day-18-Dot-Painting-Maker\\image.jpg', 30)

rgb_colors=[]
for color in colors:
    image_color = color.rgb
    rgb_colors.append(image_color)

t.colormode(255)

turtle = t.Turtle()
turtle.shape("turtle")
turtle.speed("fastest")
turtle.pensize(20)
turtle.penup()
turtle.hideturtle()

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
def draw_picture():
    for i in range(10):
        for j in range(10):
            turtle.dot(20, random.choice(rgb_colors))
            turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(500)
        turtle.setheading(0)

draw_picture()
screen = t.Screen()
screen.exitonclick()
