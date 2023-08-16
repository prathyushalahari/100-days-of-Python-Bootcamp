def turn_around():
    turn_left()
    turn_left()
    turn_left()

# variable heights present


def jump():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_around()
    else:
        turn_left()


while not at_goal():
    jump()
