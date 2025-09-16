import random
from turtle import Turtle, Screen
line = Turtle()
line.speed("fastest")
line.pensize(3)
line.color("white")
line.pencolor("red")
line.teleport(-260,260)
line.setheading(-90)
line.forward(500)
line.teleport(293,260)
line.setheading(-90)
line.forward(500)
line.hideturtle()

screen = Screen()

def actual_turtles(ycor, color):
    new_turtle = Turtle()
    new_turtle.color(color)
    new_turtle.teleport(-300, ycor)
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.shapesize(2)
    return new_turtle

list = [
actual_turtles(240,"blue"),
actual_turtles(180,"yellow"),
actual_turtles(120,"brown"),
actual_turtles(60, "green"),
actual_turtles(0,"red")
]
text = screen.textinput("Choice your Turtle","To whom you gonna bet?")
run_till = True

while run_till:
    list[random.randint(0, len(list)-1)].forward(random.randint(1,3))
    for i in list:
        if i.xcor() >= 260:
            if i.color()[0] == text:
                print(f"YAYYAYA! You Won. {text} turtle is the winner.")
            else:
                print("Ops, You Lost! Winner is ",i.color()[0])
            run_till = False

screen.exitonclick()