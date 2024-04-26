# Exercise 16: Removal all characters from a string except integers
# Given:

# str1 = 'I am 25 years and 10 months old'

# Expected Output:

# 2510
def removeCharacters(string:str):
    newString:str = ""
    for char in string:
        if char.isdigit():
            newString += char
    print(newString)

def main():
    string:str = "I am 25 years and 10 months old"
    removeCharacters(string)

if __name__=="__main__":
    main()