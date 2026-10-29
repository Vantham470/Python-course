# for loop = execute blocked of code a fixed number of time.
#            you can iterate over a range, string , sequence , etc
for x in range(1, 20): # range type for count by 2 3 ...n ( 0, 0, 2 or 3 or n....)
    print(x)

print("Happy prime day")


for x in range(1, 30):
    if x == 13:
        continue # use "continue to skip number 13" , and use "break" to count from 1 to 12 not more than 12 
    else:
        print(x)

