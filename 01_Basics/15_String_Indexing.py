# Indexing = accessing elements of sequence using [] (Indexing operator )
#            [start : end : step]

credit_number = "1234-5678-9456"

print(credit_number[0]) # output '1'
print(credit_number[0:4]) # output '1234'
print(credit_number[0:]) # output all of credit number will appear
print(credit_number[-1]) # output is 6 bc it negative so it count from back 
print(credit_number[::2]) # print second character of a string: ( or we can put it ::3, ::4 or ::n )

last_digits = credit_number[-4:] # show last numbers
print(f"XXXX-XXXX-XXXX-{last_digits}")
