# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Write your code below this line 👇

print('Welcome to the tip calculator!')

print('What was the total bill?')
bill = float(input())

# also write code like this,input acts as print also
#total_bill = float(input('What was the total bill?'))

print('How much tip would you like to give in percent? 10, 12, or 15?')
tip = float(input())
tip_percent = tip/100

print('How many people to split the bill?')
total_ppl = float(input())

total_tip = bill*tip_percent  # total tip on bill
total_bill = bill + total_tip

# total amount paid by each person
total_bill_per_person = total_bill / total_ppl


final_amount = round(total_bill_per_person, 2)
'''*above example rounds $12.567 = 12.57 but can't round off i decimal to 2 decimal always .
 eg. 12 can't be 12.00 (if we want all values to be 2 decimal places filling zeroes)

*If you want the every final_amount to always have 2 decimal places.
 e.g. $12 becomes $12.00.
You can use this link to figure out how to do this:https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python'''


print(f'Each person should pay: ${final_amount:.2f}')
# {:.2f} is used for having 2 decimal places after decimal point for given float number
