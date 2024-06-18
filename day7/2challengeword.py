import random

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)  # chooses random word

print(f'Psst,the solution is{word}.')  # CHOOSEN WORD

guess = input("Guess a letter: ").lower()  # lowers the characters

size = len(word)  # size of word

display = []  # displays empty word of '_'
for i in range(size):
    display += "_"

for index in range(0, size):
    letter = word[index]
    if guess == letter:
        display[index] = letter
print(f"{display}")
