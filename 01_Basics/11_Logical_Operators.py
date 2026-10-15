# Logical operator = evaluate multiple condition (or , and , not )
#               or = at least one condition must be true 
#              and = both condition must be true 
#              not = inverts the condition (not false , not true)

# How to use "or"
temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("We are going to play football")
else:
    print("We are stay at home")

# How to use "ended"
temp = 30
is_sunny = True

if temp >= 20 and is_sunny:
    print("It is HOT outside🌞")
    print("It is SUNNY☀️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside❄️")
    print("It is SUNNY☀️")
elif 38 > temp > 0 and is_sunny:
    print("It is WARM outside⛅️")
    print("It is SUNNY☀️")

# Usage of "Not"
if temp >= 20 and not is_sunny:
    print("It is HOT outside🌞")
    print("It is CLOUDY☁️")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside❄️")
    print("It is CLOUDY☁️")
elif 38 > temp > 0 and not is_sunny:
    print("It is WARM outside⛅️")
    print("It is CLOUDY☁️")
