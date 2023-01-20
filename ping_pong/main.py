from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("ping-pong")
screen.tracer(0)
scoreboard = ScoreBoard()
paddle_r = Paddle(350)
paddle_l = Paddle(-350)
ball = Ball()


screen.listen()
screen.onkeypress(key="Up", fun=paddle_r.up)
screen.onkeypress(key="Down", fun=paddle_r.down)
screen.onkeypress(key="w", fun=paddle_l.up)
screen.onkeypress(key="s", fun=paddle_l.down)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.change_direction_y()

    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.change_direction_x()

    if ball.xcor() > 380:
        ball.game_again()
        scoreboard.l_score += 1
        scoreboard.flush()

    if ball.xcor() < -380:
        ball.game_again()
        scoreboard.r_score += 1
        scoreboard.flush()

    ball.move()

    if (scoreboard.l_score >= 13 or scoreboard.r_score >= 13) and abs(scoreboard.l_score-scoreboard.r_score) > 1:
        game_is_on = False
        ball.hideturtle()
        scoreboard.game_over()



screen.exitonclick()
