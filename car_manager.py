from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:

            RANDOM_Y_LIST = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
            RANDOM_Y = random.choice(RANDOM_Y_LIST)
            X_START = 300
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.up()
            new_car.color(random.choice(COLORS))
            new_car.goto(X_START, RANDOM_Y)
            self.all_cars.append(new_car)

    def cars_move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

