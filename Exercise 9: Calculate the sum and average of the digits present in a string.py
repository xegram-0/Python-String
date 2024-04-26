# Exercise 9: Calculate the sum and average of the digits present in a string

# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

# Given:

# str1 = "PYnative29@#8496"

# Expected Outcome:

# Sum is: 38 Average is  6.333333333333333
def listDigit(string:str):
    numDigits: list = []
    for digit in string:
        if digit.isdigit():
            numDigits.append(digit)
    return numDigits

def stringSum(numDigits:list):
    tempDigits:list = []
    for digit in numDigits:
        tempDigits.append(int(digit))
    theSum = sum(tempDigits)
    return theSum

def stringAverage(numDigits:list):
    tempDigits:list = []
    for digit in numDigits:
        tempDigits.append(int(digit))
    theSum = sum(tempDigits)
    theAverage:float = theSum/len(numDigits)
    return theAverage

def main():
    string:str = "PYnative29@#8496"
    numDigits:list = listDigit(string)
    print(numDigits)
    print(f"Sum is {stringSum(numDigits)} and average is {stringAverage(numDigits)}")


if __name__=="__main__":
    main()

# if char.isdigit():
#         total += int(char)
#         cnt += 1

# import re

# input_str = "PYnative29@#8496"
# digit_list = [int(num) for num in re.findall(r'\d', input_str)]
# print('Digits:', digit_list)