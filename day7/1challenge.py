# guessing whether user input letter present in words present in list

import random
word_list = ["advark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter:").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
