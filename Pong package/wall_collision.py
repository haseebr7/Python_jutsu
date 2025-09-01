from turtle import Turtle

class Wall(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=40)
        self.penup()
        self.color("white")
        self.goto(0,position)