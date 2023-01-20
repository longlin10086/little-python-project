from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


timmy = Turtle()
timmy.speed('fastest')
timmy.pensize(2)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + size_of_gap)
        timmy.circle(100)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
