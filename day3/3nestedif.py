print("Welcome to the rollercoaster ride!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print(" Eligibe for Rollercoaster ride")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
    print("Sorry,Not Eligible for Rollercoaster Ride")
