# String Methods
name = input("Enter your username: ")
phone_number = input("Enter your phone number: ")
# result = len(name) # Counting character "we also can put the letter in(" ")" to find.
# result = name.find(" ") # Find the first current space of character.
# result = name.rfind(" ") # last current space.
# result = name.capitalize() # Set the first of smt capital letter. 
# result = name.upper() # All letter is capital.
# result = name.lower() # All letter is lowercase.
# result = name.isdigit # string true if we only enter number(1, 2, 3).
# result = name.isalpha # String true if we only enter the alphabetical = " no space"
# result = phone_number.count("-") # Dashes = "-"
phone_number = phone_number.replace("-", "") # use this for no dashes or with space or no space.


print(phone_number)

