'''Exercise 3 -Life in Weeks
Link: https://app.codingrooms.com/w/AZYRnfHH69lP'''

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
leftage = 90-int(age)
months = leftage*12
weeks = leftage*52
days = leftage*365
print(
    f"You have {days} days, {weeks} weeks, and {months} months left to die at 90")
