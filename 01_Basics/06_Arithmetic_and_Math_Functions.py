# New lesson we gonna learn about "Arithmetic Operator, Math function,".

# Friends = 10
# Friends = Friends + 1
# Friends += 1
# friends = friends - 2
# Friends -= 2
# Friends = Friends * 3
# Friends *= 3
# Friends = Friends / 2
# Friends /= 2
# Friends = Friends ** 2
# friends **= 2
# remainder = friends % 3
# print (remainder, Friends)

x = 3.14
y = 4
z = 5
# result = round(x)
# result = abs(y) # "aby" the absolute value of y
# result = pow(4, 3) # It mean 4*4*4=64
# result = max(x, y, z)
result = min(x, y , z)
print(result)

import math 
x = 9
print(math.pi)
print(math.e)
result = math.sqrt(x) # "sqr" = square root.
result = math.ceil(x) # In Python, ceil (short for ceiling) is a function that rounds a number up to the nearest whole number.
result = math.floor(x) #n Python, floor (from the math module) means round a number down to the nearest whole number*. 
print(result)

import math 
x = 10 
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is {round(circumference) ,2 } cm") # ​បរិមាណរង្វង់​​ = Circumference = 2 × π × r

import math 
radius = float(input("Enter the radius of circle: "))
area = math.pi * pow(radius, 2) # ផ្ទៃ​ = Area = π × r²
print(f"The area of the circle is: {round(area, 2)}cm^2")

import math 
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2)) # ពីតាគ៍រ​ = c=a2+b2
print(f"The side = {c}")
