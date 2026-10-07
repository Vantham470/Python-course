# Variable is a container for value it have: (string integers float boolean)

# #string
# we use string with (''; "")
first_name = "Levinho"
activity = "listening to music"
age = "19y"
food = "noodle"
print(f"Hello {first_name}")
print(f"In the free time you like {activity}")
print(f"You are {age}")
print(f"You like {food}")

# Integer
# For an integer we don't use (quote)
quantity = 1
num_of_student = 40
print(f"you buying {quantity}noodles")
print(f"Your class have {num_of_student}students")

# Float
# Float is a number 
price = 299.99
gpa = 90.20
distance = 16
print(f"The price is $ {price}")
print(f"Your gpa is {gpa}")
print(f"You ran for {distance}km")

# Boolean
# We use "Boolean" to create true or false
is_student = True
for_sale = False

if is_student:
    print("Your are a student now")
else:
    print("Your are not a student")

# Typecasting is the process of converting to variable from the data type str(), int(), float(), bool().
name = "Levinho"       #str
age = 19               #Int
gpa = 90.1             #float
is_student = True      #bool
# we can change any variable from str to bool to float or.
# let see the example 
age = str(age)
print(type(age))
# Do the same of this Ex if u wanna change variable from 1 to another 1.
