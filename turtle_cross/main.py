from turtle import Screen
import time

from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(player.up, "Up")
step = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move()
    
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False   
            scoreboard.game_over()
    
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        
screen.exitonclick()