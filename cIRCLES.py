import random
import turtle as t

tiny = t.Turtle()
t.colormode(255)
tiny.pensize(2)

def color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    color_selector = (r, g, b)
    return color_selector

tiny.speed("fastest")
def gap_maker(gap_size):
    for i in range(int(360/gap_size)):

        tiny.circle(100)
        tiny.color(color())
        tiny.setheading(tiny.heading() + gap_size)
        gap_size

gap_maker(70)
screen = t.Screen()
screen.exitonclick()
