import time
from turtle import Turtle,Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 20
MOVE_INCREMENT = 10
X_POS = 300
screen = Screen()
screen.tracer(0)
tim = Turtle()

tim.shape("square")
tim.shapesize(stretch_wid=1,stretch_len=2)
tim.setheading(180)
tim.penup()

time.sleep(1)

screen.update()

tim.y_po = random.randint(-230, 230)
tim.teleport(X_POS, tim.y_po)
tim.color(COLORS[random.randint(0, 5)])
tim.goto(tim.xcor() + 20,tim.ycor())
screen.exitonclick()