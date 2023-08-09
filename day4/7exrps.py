import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
user_choice = int(input(
    " What do you choose? Type 0 for Rock,1 for Paper,2 for Scissors "))
computer_choice = random.randint(0, 2)
print(f"Computer chose{computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")

if user_choice == 0:
    if computer_choice == 1:
        print("You Lose!")
    elif computer_choice == 2:
        print("You Win!")
    else:
        print("Tie")

if user_choice == 1:
    if computer_choice == 2:
        print("you lose")
    elif computer_choice == 0:
        print("you win!")
    else:
        print("Tie")

if user_choice == 2:
    if computer_choice == 2:
        print("TIE")
    else:
        print("you win!")
