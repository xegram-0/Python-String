# Exercise 18: Replace each special symbol with # in the following string
# Given:

# str1 = '/*Jon is @developer & musician!!'

# Expected Output:

# ##Jon is #developer # musician##

# import string

def replaceSpecial(string:str):
    newString:str = string
    specialString:str = "!@$%^&*()-=/"
    print(len(specialString))
    myTable = str.maketrans("!@$%^&*()-=/","############")
    print(newString.translate(myTable))
    
    # replace_char = '#'

    # string.punctuation to get the list of all special symbols
    # for char in string.punctuation:
    # str1 = str1.replace(char, replace_char)

def main():
    string:str = '/*Jon is @developer & musician!!'
    replaceSpecial(string)

if __name__=="__main__":
    main()