from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

game_on = True
while game_on:
    # Make the snake move every 0.1 seconds
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect if snake has eaten food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.reset()
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.reset()
            score.game_over()

screen.exitonclick()
