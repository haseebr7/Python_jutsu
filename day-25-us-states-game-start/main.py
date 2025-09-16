import turtle
from state_names_placer import Statefinder

screen = turtle.Screen()
screen.title("Gamer")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_finder = Statefinder()

state_finder.title()

game_on = True
while game_on:
    input_state = screen.textinput(title= state_finder.title(), prompt="Enter the state Name").title()
    if input_state == "Exit":
        state_finder.missing_states()
        break
    state_finder.state(input_state)
    print(state_finder.guessed_states)
    
screen.exitonclick()