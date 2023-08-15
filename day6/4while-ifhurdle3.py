'''REEBOK'S WORLD GAME HURDLE 3'''
'''In this case both hurdle walls and goals change for every iteration.so we need to check at next step whether wall is there or not front_is_clear()'''

# link:https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json


def turn_around():
    turn_left()
    turn_left()
    turn_left()


def hurdle():
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()
    turn_left()


while not at_goal():
    if front_is_clear() != True:
        hurdle()
    else:
        move()
