import random
from turtle import Turtle

tiny_turtle = Turtle()

tiny_turtle.shape("turtle")
tiny_turtle.pencolor("red")
tiny_turtle.penup()
tiny_turtle.goto(-10,250)
tiny_turtle.pendown()
tiny_turtle.pensize(5)

# while True:
#     tiny_turtle.forward(90)
#     tiny_turtle.right(30)
                                                       
list = [120, 90, 72, 60,  51.43, 45.0000, 40.0000, 36.0000, 32.7273, 30.0000, 27.6923, 25.7143, 24.0000, 22.5000, 21.1765, 20.0000, 18.9474, 18.0000]

num = 3
num1 = 0
while True:
    for i in range(num):
        tiny_turtle.forward(100)
        tiny_turtle.right(list[num1])
        
    num+=1
    num1 += 1
                                                  

screen = Screen()
screen.exitonclick()
