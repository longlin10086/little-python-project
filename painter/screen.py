from turtle import Screen
from cursor import Cursor
CURSOR = Cursor()


class MyScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.listen()

    def window_exit(self):
        self.screen.bye()

    def screen_action(self):
        self.screen.onkeypress(key="w", fun=CURSOR.move_forward)
        self.screen.onkeypress(key="s", fun=CURSOR.move_back)
        self.screen.onkeypress(key="a", fun=CURSOR.turn_left)
        self.screen.onkeypress(key="d", fun=CURSOR.turn_right)
        self.screen.onkey(key="c", fun=CURSOR.clear_screen)
        self.screen.onkey(key="q", fun=self.window_exit)
        self.screen.onscreenclick(CURSOR.move)

    CURSOR.cursor.ondrag(CURSOR.cursor.goto)
