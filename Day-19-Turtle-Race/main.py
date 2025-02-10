from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

for i in range(6):
    turtle=Turtle(shape="turtle")
    turtles.append(turtle)
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-230,y=-70+30*i)

if(user_bet):
    race_on=True

while race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! {winning_color} turtle won the race")
            else:
                print(f"You've lost, {winning_color} turtle won the race")
            race_on = False
        if race_on:
            rand_distance=random.randint(0,10)
            turtle.forward(rand_distance)


screen.exitonclick()
