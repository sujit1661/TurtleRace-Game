import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
player=Player()
car_m=CarManager()
score=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_m.create_car()
    car_m.move_cars()

    # detect collision with cars
    for car in car_m.all_cars:
       if car.distance(player) < 20:
           score.game_over()
           game_is_on = False

#     detect whether the player reach end or not
    if player.is_at_finish():
        player.restart()
        car_m.increase_speed()
        score.increase_level()



screen.exitonclick()
