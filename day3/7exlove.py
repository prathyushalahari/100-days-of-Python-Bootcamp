# Logical Operators : and / or / not#

# functions used lower() - to make string to lower case and count() - to count no.of alphabets in string

name = "PrAthyusha LAhari"
print(name.count('a'))
# counts only small a's but not capital ones.so make string to lower case
lower_name = "PrAthyusha LAhari".lower()
print(lower_name.count('a'))

# so always use lower() before count()

'''CODE FOR EXERCISE'''

'''Exercise 5 - Love Calculator
link:https://app.codingrooms.com/w/Po6u50fdImIJ'''

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

final_name = name1+name2
lname = final_name.lower()

true = lname.count('t')+lname.count('r')+lname.count('u')+lname.count('e')
love = lname.count('l')+lname.count('o')+lname.count('v')+lname.count('e')

score = int(str(true)+str(love))

print(f"Your Score is {score}")

if score < 10 and score > 90:
    print("you go together like coke and mentos.")
if score >= 40 and score <= 50:
    print("you are alright together.")
