# Exercise 2: Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

# Given:

# s1 = "Ault"
# s2 = "Kelly"

# Expected Output:

# AuKellylt

firstString:str = input("Enter first string: ")
secondString:str = input("Enter second string: ")

firstStringLength:int = len(firstString)
#resultString:str = firstString[0:firstStringLength//2] + secondString + firstString[firstStringLength//2:firstStringLength]

resultString:str = firstString[:firstStringLength//2] + secondString + firstString[firstStringLength//2:]
print(resultString)
