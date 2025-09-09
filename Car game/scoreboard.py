from turtle import Turtle
FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230,250)

        self.write(font=FONT, align="center", arg=f"LEVEL: {self.level}")

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(font=FONT, align="center", arg=f"LEVEL: {self.level}")

