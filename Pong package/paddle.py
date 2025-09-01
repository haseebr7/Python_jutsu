from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
                
        self.penup()
        self.shape("square")
        self.speed("fastest")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

        self.color("white")


    def up(self):
        y_new_cor = self.ycor() + 20
        self.goto(self.xcor(), y_new_cor)
    def down(self):
        y_new_cor = self.ycor() - 20
        self.goto(self.xcor(), y_new_cor)