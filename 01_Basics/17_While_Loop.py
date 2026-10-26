# while loop = executed some code WHILE some condition remain true 
#Difference btw if and while 

name = input("Enter your name: ")
if name == "":
    print("You did not enter your name")
else:
    print(f"Hello Gods {name}")

# While use to enter something like we need to do 
# if we enter nothing it will appear again and again like infinite loop but only we enter it 
name = input("Enter your name: ")
# age = int(input("Enter your age: "))
while name == "":
# while age < 0:
    print("You did not entre your name")
    name = input("Enter your name")
#   age = int(input("Enter your age: "))


print(f"Hello Gods {name}")

# infinite loop it run forever we cannot stop and scroll it to see the ended of it 
name = input("Enter your name: ")
while name == "":
    print("You did not entre your name")


print(f"Hello Gods {name}")

# we use "quit" to exit while loop or stop a code to run 

car = input("Enter a name of your favorite cars (q to quit)")

while not car == "q":
    print(f"Your favorite car is {car}")
    car = input("Enter another name of your favorite cars (q to quit)")

print("bye")

# second 
num = int(input("Enter a # between 1-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter a # between 1-10: "))

print(f"Your number is {num}")

