from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.finish = FINISH_LINE_Y
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)
    def down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
    def reset(self):
        self.teleport(0, -280)