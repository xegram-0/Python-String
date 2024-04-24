# Exercise 4: Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# Given:

# str1 = PyNaTive

# Expected Output:

# yaivePNT

str1 = "PyNaTive"
resultString:str = ""
for i in str1:
    if i.islower():
        resultString += i
        #print("Testing")

for i in str1:
    if i.isupper():
        resultString += i

# for char in str1:
#     if char.islower():
#         # add lowercase characters to lower list
#         lower.append(char)
#     else:
#         # add uppercase characters to lower list
#         upper.append(char)

# # Join both list
# sorted_str = ''.join(lower + upper)
print(resultString)