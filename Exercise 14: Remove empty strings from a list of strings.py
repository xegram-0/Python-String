# Exercise 14: Remove empty strings from a list of strings

# Given:

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# Expected Output:

# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

def removeEmptystring(stringList:list):
    for word in stringList:
        if word:
            continue
        else:
            stringList.remove(word)
    print("After removeing empty strings")
    print(stringList)

def main():
    str_list:list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    print("Orginal list of string")
    print(str_list)
    removeEmptystring(str_list)
    #new_str_list = list(filter(None, str_list))
if __name__=="__main__":
    main()