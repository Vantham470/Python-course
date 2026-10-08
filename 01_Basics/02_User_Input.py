# input() = A function that prompts to enter data 
#           Returns entered data as a string 
name = input("What is your name?: ")
age = input("How old are you?:  ")
age = int(age) # From str to int the easy one, we use this instead "age = int(input(".......")).
age = age + 1
print(f"Hello {name}!")
print("Happy Birthday to you vanntham")
print(f"Your are {age} year old!")
