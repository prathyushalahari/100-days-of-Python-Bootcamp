# while loop: While loop is infinite loop based on condition
# for loop : for loop iterates through list,range and is finite loop

'''REEBOK'S WORLD GAME HURDLE 2'''
'''In this case the final goal can be after 2nd/3rd/4th/5th hurdle.so that we check condition at_goal() if it's true , goal is present at that position'''

# link : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json


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


while not at_goal():  # at_goal!=True
    hurdle()
