import random
from random import choice
from turtle import Turtle, Screen

line = Turtle()
line.speed("fastest")
line.pensize(3)
line.color("white")
line.pencolor("red")
line.teleport(-260,260)
line.setheading(-90)
line.forward(500)
line.teleport(280,260)
line.setheading(-90)
line.forward(500)
line.hideturtle()

red_turtle = Turtle()
red_turtle.color("red")
red_turtle.teleport(-300, 260)
red_turtle.shape("turtle")
red_turtle.penup()
red_turtle.shapesize(2)

blue_turtle = Turtle()
blue_turtle.color("blue")
blue_turtle.teleport(-300, 140)
blue_turtle.shape("turtle")
blue_turtle.penup()
blue_turtle.shapesize(2)

green_turtle = Turtle()
green_turtle.color("green")
green_turtle.teleport(-300, 0)
green_turtle.shape("turtle")
green_turtle.penup()
green_turtle.shapesize(2)

run_till_then = True

while run_till_then:

    num = random.randint(1,3)

    if num == 1:
        red_turtle.forward(random.randint(1, 2))
    elif num == 2:
        blue_turtle.forward(random.randint(1, 2))
    else:
        green_turtle.forward(random.randint(1, 2))

    if red_turtle.xcor() >= 250:
        run_till_then = False
        print("Red Wins")
    elif blue_turtle.xcor() >= 250:
        run_till_then = False
        print("Blue Wins")
    elif green_turtle.xcor() >= 250:
        run_till_then = False
        print("green Wins")

screen = Screen()
screen.exitonclick()