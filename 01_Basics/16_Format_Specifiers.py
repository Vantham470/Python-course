# Format specifiers = (value:flags) format a value based on what flags are interested

price1 = 4.4443
price2 = -35505.454
price3 = 4500.45

print(f"Price 1 is ${price1:,.2f}") # 2f...nf use for to cut last number after 0.343
print(f"Price 2 is ${price2:,.2f}") # , use for a lot of number
print(f"Price 3 is ${price3:,.2f}")
