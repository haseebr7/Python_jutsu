#IGNORE IT DUDE



def turn_left():
    



def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_right()


while not at_goal():
    if wall_in front():
        jump()
    else:
        move()