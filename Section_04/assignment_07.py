# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""

#Your Code Below:



def string_match(a, b):
    count = 0 # count the number of times the substring appears in both strings
    for i in range(len(a) - 1): # -1 because we don't want to count the last character
        if a[i:i+2] == b[i:i+2]: # check if the substring appears in both strings
            count += 1 # count the number of times the substring appears in both strings
    return count

    
print(string_match('xxcaazz', 'xxbaaz')) #→ 3
print(string_match('abc', 'abc')) #→ 2
print(string_match('abc', 'axc')) #→ 0





























# Solution
# def string_match(a, b):
#     # Figure which string is shorter.
#     shorter = min(len(a), len(b))
#     count = 0
#
#     # Loop i over every substring starting spot.
#     # Use length-1 here, so can use char str[i+1] in the loop
#     for i in range(shorter - 1):
#         a_sub = a[i:i + 2]
#         b_sub = b[i:i + 2]
#         if a_sub == b_sub:
#             count = count + 1
#
#     return count
