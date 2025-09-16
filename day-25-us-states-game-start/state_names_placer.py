from turtle import Turtle, Screen
import pandas
GUESSED_STATES = []

class Statefinder(Turtle):
    def __init__(self,):
        super().__init__()
        screen = Screen()
        self.penup()
        self.speed("fastest")
        self.guessed_states = len(GUESSED_STATES)
        self.missed_states = []

    def state(self,input_state):
        states = pandas.read_csv("50_states.csv")
        num = 0
        for i in states.state:

            if input_state == i:
                guessed_state = states[states.state == input_state]
                name = guessed_state.state[num]
                x_cor = guessed_state.x[num]
                y_cor = guessed_state.y[num]

                self.goto(x_cor, y_cor)
                self.write(f"{name}", align="center", font=("arial", 8, "normal"))
                print("i",x_cor,y_cor)
                global GUESSED_STATES
                if name in GUESSED_STATES:
                    pass
                else:
                    GUESSED_STATES.append(name)
                print(GUESSED_STATES)
                print(len(GUESSED_STATES))

            num += 1

    def title(self):
        return f"{len(GUESSED_STATES)}/50"

    def missing_states(self):
        states = pandas.read_csv("50_states.csv")
        for i in states.state:
            if i in GUESSED_STATES:
                pass
            else:
                self.missed_states.append(i)

        with open("Missing_states.txt", "w") as file:
            for i in self.missed_states:
                file.write(f"{i}\n")