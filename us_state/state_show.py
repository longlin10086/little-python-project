from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 10, "normal")


class ShowState:
    def __init__(self):
        self.state_list = []

    def creat_state(self, position, name):
        new_state = Turtle()
        new_state.penup()
        new_state.color("black")
        new_state.speed("fastest")
        new_state.hideturtle()
        new_state.goto(position)
        new_state.write(name, align=ALIGNMENT, font=FONT)
        self.state_list.append(new_state)

