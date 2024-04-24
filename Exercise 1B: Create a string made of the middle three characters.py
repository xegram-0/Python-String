# Exercise 1B: Create a string made of the middle three characters
yourString : str = input("Enter your string: ")
stringLength : int = len(yourString)
newString : str = yourString[(stringLength//2)-1] + yourString[stringLength//2] + yourString[(stringLength//2)+1]
# res = str1[mi - 1:mi + 2]
print(f"Your new string is {newString}")