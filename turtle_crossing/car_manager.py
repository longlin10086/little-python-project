from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.distance = STARTING_MOVE_DISTANCE
        self.level = 1

    def create_cars(self):
        random_choice = random.randint(1, 6)
        if random_choice <= self.level:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randrange(-240, 240, 20))
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.backward(self.distance)

    def clear_screen(self):
        for car in self.car_list:
            car.hideturtle()

    def add_level(self):
        self.level += 1
        self.distance += MOVE_INCREMENT

