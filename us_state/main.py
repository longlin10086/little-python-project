import turtle
import pandas
from state_show import ShowState


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
data_primary = pandas.read_csv("50_states.csv")
state_list = data_primary["state"].to_list()
state_list_ignore = []
answer = []
state = ShowState()

screen.addshape(image)
turtle.shape(image)

is_on_game = True
while is_on_game:
    answer_state = screen.textinput(title="Guess the State",
                                    prompt=f"What's another state's name?({len(state.state_list)}/50)").title()
    if answer_state in state_list:
        answer.append(answer_state)
        x = int(data_primary[data_primary['state'] == answer_state].x)
        y = int(data_primary[data_primary['state'] == answer_state].y)
        position = (x, y)
        state.creat_state(position=position, name=answer_state)
    if answer_state[0] == "Q" or len(state.state_list) >= 50:
        is_on_game = False

for item in state_list:
    if item not in answer:
        state_list_ignore.append(item)

df = pandas.DataFrame(state_list_ignore)
df.to_csv("missing_state.csv")
turtle.exitonclick()
