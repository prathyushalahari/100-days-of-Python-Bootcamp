'''Exercise 2 - Banker Roulette
LINK:https://app.codingrooms.com/w/jpELJA3H42p1'''
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")  # list
# .split() splits input into seperate elements as list
size = len(names)  # size of list
pick_random_index = random.randint(0, size-1)
# ammprint(pick_random_index)
pick_random_person = names[pick_random_index]

# OR ANOTHER TECHNIQUE using .choice() gives random element from list directly
pick_random_person1 = random.choice(names)
print(pick_random_person+" is going to buy meal today")
