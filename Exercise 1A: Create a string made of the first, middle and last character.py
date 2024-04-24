# Exercise 1A: Create a string made of the first, middle and last character
name:str = input("Enter your name: ")
print(f"Hello, {name}")
newString:str = name[0] + name[len(name)//2] + name[-1]
print(f"Your new string is {newString}")
