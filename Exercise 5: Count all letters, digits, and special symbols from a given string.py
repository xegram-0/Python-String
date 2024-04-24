# Exercise 5: Count all letters, digits, and special symbols from a given string

# Given:

# str1 = "P@#yn26at^&i5ve"

# Expected Outcome:

# Total counts of chars, digits, and symbols 

# Chars = 8 
# Digits = 3 
# Symbol = 4

str1 = "P@#yn26at^&i5ve"
countChars:int = 0
countDigits:int = 0
countSymbol:int = 0

for i in str1:
    if i.isalpha():
        countChars+=1
    elif i.isdigit():
        countDigits+=1
    else:
        countSymbol+=1

print(f"Chars = {countChars} \nDigits = {countDigits} \nSymbol = {countSymbol}")


