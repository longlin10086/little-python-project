from turtle import Turtle
import time
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.history_score = 0
        self.score = 0
        self.color('black')
        self.penup()
        self.count_down()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        if self.score > self.history_score:
            self.history_score = self.score
        self.write(f"Score: {self.score}  history highest score:{self.history_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
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

    def scoreboard_again(self):
        self.score = 0
        self.clear()
        self.count_down()
        self.goto(0, 270)
        self.update_scoreboard()
