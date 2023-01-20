import time
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.count_down()
        self.l_score = 0
        self.r_score = 0
        self.flush()

    def flush(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        if self.r_score > self.l_score:
            self.write("The right win!", align=ALIGNMENT, font=("Courier", 50, "normal"))
        else:
            self.write("The left win!", align=ALIGNMENT, font=("Courier", 50, "normal"))
        time.sleep(3)
        self.clear()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def count_down(self):
        self.goto(0, 0)
        self.write(3, align=ALIGNMENT, font=FONT)
        self.clear()
        time.sleep(1)
        self.write(2, align=ALIGNMENT, font=FONT)
        self.clear()
        time.sleep(1)
        self.write(1, align=ALIGNMENT, font=FONT)
        self.clear()
        time.sleep(1)
        self.write("BEGIN!", align=ALIGNMENT, font=FONT)
        time.sleep(0.5)
        self.clear()
