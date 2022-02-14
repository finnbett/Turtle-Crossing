import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
bob = Player()
screen.listen()
screen.onkey(bob.move_up, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
game_speed = 0.1
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    car_manager.create_car()
    car_manager.cars_move()
    scoreboard.display_score()
    if bob.ycor() > 270:
        bob.goto(player.STARTING_POSITION)
        scoreboard.level_up()
        game_speed *= 0.5

    for car in car_manager.all_cars:
        if bob.distance(car) < 30:
            game_is_on = False
screen.clear()
scoreboard.game_over()
screen.exitonclick()
