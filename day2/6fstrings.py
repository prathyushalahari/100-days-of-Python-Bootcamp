
score = 0  # type = int
height = 1.8  # type = float
isWinning = True  # type = boolean

# covert above 3 variables into string format to print.
print("your score is "+str(score)+", height  " +
      str(height) + "and winning is "+str(isWinning))

# but above print is tedious process

'''So,Inorder to avoid lengthy print statements,we use f-strings'''

print(f"your score is {score}, height is {height} and winning is {isWinning}")

'''these curly braces {} in f-strings automatically take care of typecasting, so we do not need to convert any'''


# formatting decimal places
'''https: // www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python'''
