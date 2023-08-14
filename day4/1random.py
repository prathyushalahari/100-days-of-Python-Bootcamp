'''Generating random numbers is two kinds'''
# repeated random sequence 5 4 3 9 4 3 9 4 ...this randomness repeats after sometime'''
# pseudo random sequence 5 3 4 5 6 7 2 1 8 9 4 3 ..doesn't repeat any cycle
'''python follows repeated random sequence in given range'''

# imports random module
import random
find_random_no = random.randint(1, 10)
print(find_random_no)
# .randint() gives random integer in given range

find_random_float = random.random()  # works only b/w 0 to 1
# .random() always gives random float between 0.000000 to 9.999999
print(find_random_float)

'''How to get a random float b/w 0 to 5?'''
find_random_float2 = random.random()*5  # multiply by end integer:5
print(find_random_float2)

# OR ANOTHER TECHNIQUE using .choice() gives random element from list directly
pick_random_item_from_list = random.choice(list_name)
