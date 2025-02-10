from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# paddle setups
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
# ball setup
ball = Ball()
# scoreboard setup
scoreboard = Scoreboard()

screen.listen()
# right paddle controls
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

# left paddle controls
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

# game loop
game_on = True
sleep_time = 0.005
while game_on:
    screen.update()
    ball.move_ball()
    # check for walls
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
        sleep_time = ball.move_speed
    # check for paddles
    if ball.xcor() == 340 and ball.distance(right_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() == -340 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
    # right side miss
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()
        sleep_time = ball.move_speed
    # left side miss
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()
        sleep_time = ball.move_speed


    time.sleep(sleep_time)

screen.exitonclick()
