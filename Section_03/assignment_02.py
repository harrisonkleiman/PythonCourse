# Assignment 2:
"""
    create a function called separate() that accepts a string as an argument
    and returns a list containing each of the characters of
    the string separated as individual items in the list.

    Make sure to test the function.
"""
# Your Code Below:

def separate(string):
    list = []
    for char in string:
        list.append(char)
    return list

# Test Code Below:

print(separate("hello"))

# Output:
# ['h', 'e', 'l', 'l', 'o']











































# Solution Below:

# def separate(str):
#     return list(str)
#
# print(separate("hello there"))