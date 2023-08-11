'''SIMPLE FOR LOOP'''

fruits = ["Apple", "Peach", "Pear"]
for element in fruits:
    print(element)  # element
    print(element + " Pie")  # element+string
    print(fruits)  # list in forloop

# looping in range
for number in range(1, 11):
    print(number)

# looping using range and step
for number in range(1, 11, 3):
    print(number)

# sum of given range
total = 0
for number in range(1, 101):
    total += number
print(total)
