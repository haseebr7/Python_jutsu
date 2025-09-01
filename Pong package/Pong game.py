from scoreboard import Scoreboard
import time

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from wall_collision import Wall

screen = Screen()
screen.title("Pong Game")
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
score = Scoreboard()
ball = Ball()
u_wall = Wall(-290)
d_wall = Wall(300)

game_on_hai = True

while game_on_hai:


    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 270 or ball.ycor() < -260:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 360:
        ball.reset_ball()
        score.l_update()
    if ball.xcor() < -360:
        ball.reset_ball()
        score.r_update()


screen.exitonclick()