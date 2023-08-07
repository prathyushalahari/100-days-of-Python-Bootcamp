# Exercise 2 - BMI Calculator
# link : https://app.codingrooms.com/w/3mJPclekl98T

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
w = float(weight)
h = float(height)
bmi = w/(h*h)
roundoff_bmi = int(bmi)
print(roundoff_bmi)
name = input("what is your name ")
