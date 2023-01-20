import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgcolor("black")
turtle.title("Snaking")
screen.tracer(0)
screen.bgpic('pic.png')

food_list = []
snake = Snake()
for _ in range(6):
    food = Food()
    food_list.append(food)
board = ScoreBoard()


is_on_game = True
while is_on_game:
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.update()
    time.sleep(0.1)
    snake.move()

    for food in food_list:
        if snake.head.distance(food) < 15:
            snake.extend()
            for segment in snake.segments:
                segment.color(food.color()[0])
            food.refresh()
            board.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_on_game = False
        board.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_on_game = False
            board.game_over()

    if not is_on_game:
        user_answer = screen.textinput(title="AGAIN", prompt="Do you want to play again? Type 'yes' or 'no'.").lower()
        if user_answer[0] == 'y':
            is_on_game = True
            snake.snake_again()
            board.scoreboard_again()

screen.exitonclick()
