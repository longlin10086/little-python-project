from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ").lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []


for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + 30 * i)
    turtle_list.append(new_turtle)


is_race_on = bool(user_bet)
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.color()[0] == user_bet:
                print(f"You win! The winner is the {turtle.color()[0]} one.")
            else:
                print(f"You lose! The winner is the {turtle.color()[0]} one.")

    for turtle in turtle_list:
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)


screen.exitonclick()
