'''1) typechecking - checking data type'''

num_char1 = len(input("give name to find it's length?\n"))
print(num_char1)  # length

num_char_type = type(len(input("give name to find it's type?\n")))
print(num_char_type)  # type


'''2)typecasting/typeconversion - 
converting variable data from one data type to other data type'''

num_char2 = len(input("Name please?\n"))  # takes length
new_num_char = str(num_char2)  # conversion int length->string length
print("Your Name has "+new_num_char+" characters.")
# we can only concatenate str (not "int") to str. so converted numchar2 to sting newnumchar

print("identify below type")
# examples
a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(123)
print(type(a))

# add 70 and 100 by int,str,float
print(70+100)
print(70+float("100.5"))
print(str(70)+str(100))
