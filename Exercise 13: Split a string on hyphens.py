# Exercise 13: Split a string on hyphens

# Write a program to split a given string on hyphens and display each substring.

# Given:

# str1 = Emma-is-a-data-scientist

# Expected Output:

# Displaying each substring

# Emma
# is
# a
# data
# scientist

def displaySubstring(string:str):
    subString:list = []
    subString = string.split("-")
    #print(type(string.split("-")))
    for word in subString:
        print(word)
def main():
    string:str = "Emma-is-a-data-scientist"
    displaySubstring(string)
if __name__=="__main__":
    main()