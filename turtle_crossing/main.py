import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

car = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkeypress(key="Up", fun=player.move)
    car.create_cars()
    car.move()
    scoreboard.update_timeboard()
    time.sleep(0.1)
    screen.update()

    for one_car in car.car_list:
        if player.distance(one_car) < 30 or scoreboard.crossing_time >= 300:
            game_is_on = False
            car.clear_screen()
            scoreboard.game_over()
            screen.update()

    if player.check_again():
        scoreboard.adding_time()
        scoreboard.increase_score()
        car.add_level()

    if not game_is_on:
        user_answer = screen.textinput(title="AGAIN", prompt="Do you want to play again? Type 'yes' or 'no'.").lower()
        if user_answer[0] == 'y':
            game_is_on = True
            car.game_again()
            player.player_again()
            scoreboard.scoreboard_again()
            screen.update()


screen.exitonclick()
