# Exercise 1 - Data Types
# link : https://app.codingrooms.com/w/rBSqejz5SfNE

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# Write your code below this line 👇
print(type(two_digit_number))
# convert string twodigitnumber to int

# ERROR
#new_two_digit_number = int(two_digit_number)
# print(new_two_digit_number[0]+new_two_digit_number[1])

'''above print gives error, new_two_digit_number is not a string array(it's int) to retrieve element at any index, only string arrays can retrieve elements using index(called subcript).'int' object is not subscriptable'''

# SO CONVERT EACH DIGIT TO INT
firstno = int(two_digit_number[0])
secondno = int(two_digit_number[1])
r = firstno + secondno

print(r)
print('after typecast :')
print(type(r))
'''so we need to individually convert every string character(numbers) to integer to perform addition'''
