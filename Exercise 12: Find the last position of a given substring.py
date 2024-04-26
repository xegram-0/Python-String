# Exercise 12: Find the last position of a given substring

# Write a program to find the last position of a substring “Emma” in a given string.

# Given:

# str1 = "Emma is a data scientist who knows Python. Emma works at google."

# Expected Output:

# Last occurrence of Emma starts at index 43


def lastLocation(string:str,subString:str):
    indexLocation:int = string.rfind(subString)
    return indexLocation
def main():
    string:str ="Emma is a data scientist who knows Python. Emma works at google."
    subString:str = "Emma"
    print(lastLocation(string,subString))

if __name__=="__main__":
    main()