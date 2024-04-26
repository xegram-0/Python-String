# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case

# Write a program to find all occurrences of “USA” in a given string ignoring the case.

# Given:

# str1 = "Welcome to USA. usa awesome, isn't it?"

# Expected Outcome:

# The USA count is: 2

def findSubstring(string: str, word: str):
    count = 0
    # for word in string:
    #     if word in string:
    #         count += 1

    # Finding all cases
    count = string.lower().count(word.lower())

    return count

def main():
    string:str = "Welcome to USA. usa anwsome, isn't it?"
    word:str = "usa"
    print(f"The {word} count is {findSubstring(string,word)}")

if __name__=="__main__":
    main()