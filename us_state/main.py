import turtle
import pandas
from state_show import ShowState


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
data_primary = pandas.read_csv("50_states.csv")
state_list = data_primary["state"].to_list()
state = ShowState()

screen.addshape(image)
turtle.shape(image)

is_on_game = True
while is_on_game:
    answer_state = screen.textinput(title="Guess the State", prompt=f"What's another state's name?({len(state.state_list)}/50)")
    if answer_state in state_list:
        x = int(data_primary[data_primary['state'] == answer_state].x)
        y = int(data_primary[data_primary['state'] == answer_state].y)
        position = (x, y)
        state.creat_state(position=position, name=answer_state)
    if answer_state[0] == "q":
        is_on_game = False

turtle.exitonclick()
