from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed("fastest")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.color("black")
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def check_again(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False

    def player_again(self):
        self.hideturtle()
        self.setposition(STARTING_POSITION)
        self.showturtle()
