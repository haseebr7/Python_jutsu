from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

position = 0
def forward():
    tim.forward(20)
def backward():
    tim.backward(20)
def right():
    global position
    position -= 10
    tim.setheading(position)
def left():
    global position
    position += 10
    tim.setheading(position)
def clear_it():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def up():
    tim.penup()

def down():
    tim.pendown()

screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=right, key="d")
screen.onkey(fun=left, key="a")
screen.onkey(fun=clear_it, key="c")
screen.onkey(fun=up, key="q")
screen.onkey(fun=down, key="e")


screen.exitonclick()
