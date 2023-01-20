from turtle import Turtle
import time
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.time = time.time()
        self.crossing_time = 0
        self.level = 1
        self.color('black')
        self.penup()
        self.count_down()
        self.update_scoreboard()
        self.update_timeboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def update_timeboard(self):
        self.clear()
        self.goto(280, 260)
        self.crossing_time = round(time.time()-self.time)
        self.write(f"Left time: {300-self.crossing_time}s", align='right', font=FONT)
        self.update_scoreboard()

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

    def scoreboard_again(self):
        self.time = time.time()
        self.crossing_time = 0
        self.level = 1
        self.clear()
        self.count_down()
        self.goto(-280, 260)
        self.update_scoreboard()

    def adding_time(self):
        self.time += 20
