from turtle import Turtle
import random
import time


def random_number():
    if random.randint(0, 1) == 0:
        if random.randint(0, 1) == 0:
            return random.randint(10, 75)
        else:
            return random.randint(285, 350)
    else:
        return random.randint(105, 255)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.speed("fastest")
        self.penup()
        self.setheading(random_number())
        self.move_speed = 0.05

    def move(self):
        self.forward(20)

    def change_direction_x(self):
        angle = 180 - self.heading()
        self.setheading(angle)
        self.move_speed *= 0.9

    def change_direction_y(self):
        angle = 360 - self.heading()
        self.setheading(angle)
        self.move_speed *= 0.95

    def game_again(self):
        self.setposition(0, 0)
        self.move_speed = 0.05
        time.sleep(0.1)
        self.setheading(random_number())

