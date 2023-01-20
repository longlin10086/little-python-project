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

screen.listen()
screen.onkeypress(key="Up", fun=player.move)
game_is_on = True
while game_is_on:
    car.create_cars()
    car.move()
    time.sleep(0.1)
    screen.update()

    for one_car in car.car_list:
        if player.distance(one_car) < 30:
            game_is_on = False
            car.clear_screen()
            scoreboard.game_over()
            screen.update()

    if player.check_again():
        scoreboard.increase_score()
        car.add_level()

screen.exitonclick()
