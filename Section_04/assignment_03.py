# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""

# Your Code Below:

def sequence(list):
    for i in range(len(list) - 2): # -2 because we need to check 
                                   #the next 2 elements
        if list[i] == 1 and list[i + 1] == 2 and list[i + 2] == 3:
            return True
    return False

# Test Code Below:

print(sequence([1, 1, 2, 3, 1])) # True
print(sequence([1, 1, 2, 4, 1])) # False
print(sequence([1, 1, 2, 1, 2, 3])) # True































# Solution:

# def sequence(num_list):
#     # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False
