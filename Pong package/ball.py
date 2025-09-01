from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.move_speed *= 0.9
        self.x_move *= -1


    def reset_ball(self):
        self.teleport(0,0)
        self.move_speed = 0.1
        time.sleep(0.5)
        self.x_bounce()

