import random

word_list = ["ardvark", "baboon", "camel"]

word = random.choice(word_list)

print(f'Psst,the solution is{word}.')

guess = input("Guess a letter: ").lower()

size = len(word)

display = []
for i in range(size):
    display += "_"

for index in range(0, size):
    letter = word[index]
    if guess == letter:
        display[index] = letter
print(f"{display}")
