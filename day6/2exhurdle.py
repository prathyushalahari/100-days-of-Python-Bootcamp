'''REBORG'S WORLD HURDLE1'''
# LINK:https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


def turn_around():
    turn_left()
    turn_left()
    turn_left()


def hurdle():
    move()
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()
    turn_left()


'''hurdle()
hurdle()
hurdle()
hurdle()
hurdle()
hurdle()'''

for step in range(1, 7):
    hurdle()
    jump()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
