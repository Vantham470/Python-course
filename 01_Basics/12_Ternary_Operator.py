# Condition1 expression = A one - line shortcut fo the "if - else" statement (Ternaary operator)
#                          print or assign of two value based on condition
#                          formula = "X if condition else Y"
num = 5 
a = 6 
b = 10 
age = 19
temperature = 16
user_role = "Admin Vantham!"
print("positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature > 38 else "COULD"
access_level = "Full access" if user_role == "Admin" else "Limited access"

print(result)
print(max_num)
print(min_num)
print(status)
