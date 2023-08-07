# add
print(4+3)

# sub
print(4-3)

# mul
print(4*3)

# divison always gives o/p in float
print(4/3)
print(4/2)

# power
print(4**3)

# order of execution in python
# PEMDASLR
'''
Parenthsis:  ()
Exponents :  **
Multiplication :  *
Divison :  /
Addition :  +
Subtraction: -
Left to Right approach
'''
# but * and / have same priority
print(3 * 3 + 3 / 3 - 3)
print(3 / 3 + 3 * 3 - 3)

# likewise + and -
print(3 + 3 - 3 / 3 * 3)
print(3 - 3 + 3 / 3 * 3)

# roundoff integers
print(round(8/3))  # nearer to biggest no.
print(8//3)  # floor divison
print(round(2.666666, 2))  # roundsoff 2 decimal places

# mathematical expressions
score = 0
score += 1
score /= 2
score -= 1
score *= 2
