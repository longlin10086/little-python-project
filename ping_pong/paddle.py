from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color('white')
        self.speed("fastest")
        self.penup()
        self.x_pos = x_pos
        self.y_pos = 0
        self.goto(self.x_pos, self.y_pos)

    def up(self):
        if self.ycor() < 300:
            new_y = self.ycor() + 50
            self.goto(self.x_pos, new_y)

    def down(self):
        if self.ycor() > -300:
            new_y = self.ycor() - 50
            self.goto(self.x_pos, new_y)
