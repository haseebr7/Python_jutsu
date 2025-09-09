import random
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
score1 = Scoreboard()


car.cars()
game_is_on = True
while game_is_on:
    print(len(car.all_cars))
    car.move()

    if random.randint(1,18) == 3:
        car.cars()

    car.move()

    for i in car.all_cars:
        if i.distance(player) < 30:
            game_is_on = False

    time.sleep(0.05)
    screen.update()

    screen.listen()
    screen.onkey(player.up,"w")
    screen.onkey(player.down,"s")
    if player.ycor() > player.finish:
        car.level_up()
        player.reset()
        score1.level_up()
        # faw