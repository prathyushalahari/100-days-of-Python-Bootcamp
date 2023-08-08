'''LISTS DATA structure'''
state1 = "Rajasthan"
state2 = "Assam"

states_of_India = ["AP", "Telangana",
                   "Tamil nadu", "Gujarat", "Karnataka", "Kerala"]
print(states_of_India)

print(states_of_India[0])
print(states_of_India[1])

# Lists always start with Index '0'

print(states_of_India[-1])
# prints last element from list

# to modify any data in list
states_of_India[0] = "Andhra Pradesh"
print(states_of_India[0])


# to add any data to list
states_of_India.append("Punjab")
print(states_of_India)

# extending list with more than one data
states_of_India.extend(["MANIPUR", "NAGALAND"])

print(states_of_India)

'''We can more functions used for lists in documentation : https://docs.python.org/3/tutorial/datastructures.html'''
