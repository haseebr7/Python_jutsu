import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen1 = Screen()
screen1.setup(600,600)
screen1.bgcolor("black")
screen1.tracer(0)

snake = Snake()
food = Food()
actual_score = Scoreboard()


screen1.listen()
screen1.onkey(snake.up,"Up")
screen1.onkey(snake.down,"Down")
screen1.onkey(snake.right, "Right")
screen1.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen1.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        actual_score.score +=1
        actual_score.write_score()
        snake.extend_snake()
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        actual_score.game_over()

    for i in snake.segments[1:]:

        if snake.head.distance(i) < 10:
            game_is_on = False
            actual_score.game_over()

screen1.exitonclick()