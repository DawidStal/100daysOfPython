import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")
car_manager.add_car()

count=0
game_is_on = True
while game_is_on:
    count += 1

    if player.ycor() > 280:
        player.reset_position()
        car_manager.next_level()
        scoreboard.next_level()

    if count % 6 == 0:
        car_manager.add_car()
        count = 0

    for car in car_manager.cars:
        if player.check_collision(car):
            scoreboard.game_over()
            game_is_on = False
        car_manager.move_car(car)

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
