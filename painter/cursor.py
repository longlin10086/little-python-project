from turtle import Turtle
ANGLE = 0


class Cursor:
    def __init__(self):
        self.cursor = Turtle()
        self.cursor.pensize(10)

    def move_forward(self):
        self.cursor.forward(10)

    def move_back(self):
        self.cursor.forward(-10)

    def turn_left(self):
        global ANGLE
        ANGLE += 5
        self.cursor.setheading(ANGLE)

    def turn_right(self):
        global ANGLE
        ANGLE -= 5
        self.cursor.setheading(ANGLE)

    def clear_screen(self):
        self.cursor.setheading(0)
        self.cursor.setposition(0, 0)
        self.cursor.clear()

    def move(self, x, y):
        self.cursor.penup()
        self.cursor.goto(x, y)
        self.cursor.pendown()

