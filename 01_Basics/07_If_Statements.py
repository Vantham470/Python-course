# if = Do some code only IF some condition is True
#      Else do something else 
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up")
elif age >= 0:
    print("You are not born yet")
elif age >= 1000: # This is not running until you change "age >=100".
    print("You are too old to sign up")
else:
    print("Your are too young to sign up")

# New
response = input("Would you like to have some food? (Y/N): ")

if response == "Y":
    print("Ohh sweetie you got some food here!")
else:
    print("No food for you stupid bastard!")

# New
name = input("Enter your name: ")

if name == "":
    print("You have not enter your name yet!")
else:
    print(f"Hello prime's {name} your are back!")
