# Exercise 15: Remove special symbols / punctuation from a string

# Given:

# str1 = "/*Jon is @developer & musician"

# Expected Output:

# "Jon is developer musician"
def removeSpecial(string:str):
    newString:str = string
    # for char in string:
    #     if char.isalpha():
    #         newString += char
    #         newString += " "
    #     elif char.isdigit():
    #         newString += char
    #         newString += " "
    #     else:
    #         continue
    specialString:str = "!@#$%^&*()-=/"
    myTable = str.maketrans('','',specialString)
    # Using string.punctuation removes all the special characters
    # without worrying the error of escaping characters
    # importing from string 
    print(newString.translate(myTable))

def main():
    string:str = "/*Jon is @developer & musician"
    removeSpecial(string)

if __name__=="__main__":
    main()