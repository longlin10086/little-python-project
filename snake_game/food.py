from turtle import Turtle
import random


colors = ['lightcoral', 'orange', 'gold', 'lightgreen', 'lightskyblue', 'Mediumpurple', 'pink', 'Khaki']


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(colors))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.color(random.choice(colors))
        self.goto(random_x, random_y)
