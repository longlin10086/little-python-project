from turtle import Turtle
import time
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.count_down()
        self.goto(-280, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def count_down(self):
        self.goto(0, 0)
        self.write("3", align=ALIGNMENT, font=FONT)
        self.clear()
        time.sleep(1)
        self.write("2", align=ALIGNMENT, font=FONT)
        self.clear()
        time.sleep(1)
        self.write("1", align=ALIGNMENT, font=FONT)
        self.clear()
        time.sleep(1)
        self.write("BEGIN!", align=ALIGNMENT, font=FONT)
        time.sleep(0.5)
        self.clear()
