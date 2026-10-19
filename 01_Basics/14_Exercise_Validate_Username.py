# Exercise
# Validate user input 
# 1. User name is no more than 12 character
# 2. Name must not contain space
# 3. Name must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can't be more than 12 character")
elif not username.find(" ") == -1:
    print("Your username can't contain space")
elif not username.isalpha():
    print("Your username can't contain number")
else:
    print(f"Welcome {username}")

