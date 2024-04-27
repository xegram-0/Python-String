# Exercise 17: Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.

# Given:

# str1 = "Emma25 is Data scientist50 and AI Expert"

# Expected Output:

# Emma25
# scientist50

def findWords(string:str):
    listWords:list = []
    # Chop the long string into sub-strings with word
    temp:list = string.split()
    #print(temp)

    for word in temp:
        # This part is harder to understand
        # char is temporary variable for the testing like str.translate()
        # Comprehension in any()
        if any(char.isalpha() for char in word) and any(char.isdigit() for char in word):
            #print(char)
            listWords.append(word)
    print(listWords)

def main():
    string:str = "Emma25 is Data scientist50 and AI Expert"
    findWords(string)

if __name__=="__main__":
    main()