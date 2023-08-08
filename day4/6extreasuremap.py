'''Exercise 3 - Treasure Map
https://app.codingrooms.com/management/assignments/364931/overview'''

# Map has Nested Lists .  map=[list1,list2,list3]

row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
# map = [[o,o,o],[o,o,o],[o,o,o]]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")  # 23

# Write your code below this row 👇
col = int(position[0])-1  # 2nd col
row = int(position[1])  # 3rd row

map[row-1][col] = "X"


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
