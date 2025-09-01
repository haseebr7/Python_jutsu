from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):   # correct constructor
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_score()
        self.font_size = 34
    def update_score(self):
        self.clear()
        self.goto(80,220)
        self.write(f"{self.r_score}", align="center", font=("Arial", 32, "bold"))
        self.goto(-80,220)
        self.write(f"{self.l_score}", align="center", font=("Arial", 32, "bold"))

    def r_update(self):
        self.r_score += 1
        self.update_score()

    def l_update(self):
        self.l_score += 1   # fixed
        self.update_score()
