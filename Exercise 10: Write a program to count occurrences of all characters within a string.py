# Exercise 10: Write a program to count occurrences of all characters within a string

# Given:

# str1 = "Apple"

# Expected Outcome:

# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

def findOccurrences(string:str):
    char_list:dict = dict()
    count:int = 0
    for char in string:
        count = string.count(char)
        #print(count)
        char_list[char] = count
    return char_list
def main():
    theString:str = "Apple"
    print(findOccurrences(theString))

if __name__=="__main__":
    main()
