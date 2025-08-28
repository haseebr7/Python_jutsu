import random
import turtle as t

tiny = t.Turtle()
t.colormode(255)
tiny.pensize(5)

def colora():
    r = random.randint(0, 10)
    g = random.randint(0, 10)
    b = random.randint(0, 10)
    return (r, g, b)


tiny.speed("fastest")
tiny.circle(100)


# while True:
#     tiny.forward(20)
#     direction = random.choice(["left", "right", "straight"])
#     tiny.pencolor(colora())
#
#     if direction == "left":
#         tiny.left(random.randint(0, 255))
#     elif direction == "right":
#         tiny.right(random.randint(0, 255))
#     # straight means no turn

screen = t.Screen()
screen.exitonclick()
