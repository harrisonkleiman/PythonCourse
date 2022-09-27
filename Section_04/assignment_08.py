# Assignment 8

"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""

#Your Code Below:
def sum_78(list):
    sum = 0 # initialize sum
    i = 0 # initialize i
    while i < len(list): # loop through the list
        if list[i] == 7: # if the element is 7
            while list[i] != 8: # loop until the element is 8
                i += 1 # increment i
        else: # if the element is not 7
            sum += list[i] # add the element to the sum
        i += 1 # increment i
    return sum 

# Test Code Below:

print(sum_78([1, 2, 2])) # 5
print(sum_78([1, 2, 2, 7, 99, 99, 8])) # 5
print(sum_78([1, 1, 7, 8, 2])) # 4
    















print(sum_78([1, 2, 2])) #→ 5
print(sum_78([1, 2, 2, 7, 99, 99, 8])) #→ 5
print(sum_78([1, 1, 7, 8, 2])) #→ 4



























# Solution:

# def sum78(nums):
#     sum = 0
#     inRange = False
#
#     for i in range(len(nums)):
#         if nums[i] == 7:
#             inRange = True
#
#         if not inRange:
#             sum += nums[i]
#
#         if inRange and nums[i] == 8:
#             inRange = False
#
#     return sum