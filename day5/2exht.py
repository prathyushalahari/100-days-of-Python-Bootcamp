'''Exercise 1 - Average Height'''
'''https://app.codingrooms.com/w/w7MmKk8WxSOJ'''

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
total_height = 0
no = 0
avg = 0
for height in student_heights:
    total_height += height
    no += 1
avg = total_height/no
print(avg)
