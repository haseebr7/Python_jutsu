from turtle import Screen, Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,250)
        self.color("white")
        self.penup()
        self.write_score()
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center",font=("Agency FB", 36, "bold"))

    def write_score(self):
        self.clear()
        self.write(f"Current Score: {self.score}", align="center", font=("Agency FB", 16, "bold"))
