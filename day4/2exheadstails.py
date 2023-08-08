'''Exercise 1 - Heads or Tails
LINK : https://app.codingrooms.com/management/assignments/364927/overview '''

# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
import random

toss_no = random.randint(0, 1)
if toss_no == 0:
    print("Heads")
else:
    print("Tails")
