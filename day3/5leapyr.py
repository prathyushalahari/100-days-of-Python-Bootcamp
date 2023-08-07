'''Exercise 3 - Leap Year
link: https://app.codingrooms.com/management/assignments/364924/overview
logic behind it : check flow chart in above link'''

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(" Century Leap year.")  # 2000,2400,2800
        else:
            print('Not Leap year')  # 2100,2300
    else:
        print('NLeap year.')  # 2012,2004
else:
    print('Not leap year.')  # 2013,2017
