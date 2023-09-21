""" 
Create a function that takes a list of integers and a group length as parameters. Your task is to determine if it's possible to split all the numbers from the list into groups of the specified length, while ensuring that consecutive numbers are present within each group.

Input
lst: A list of integers representing the numbers to be divided into groups.

group_len: An integer indicating the desired length of each group.

Output
The function should return True if it's possible to create groups according to the criteria, and False otherwise.

Examples
consecutive_nums([1, 3, 5], 1) ➞ True
# It is always possible to create groups of length 1.

consecutive_nums([5, 6, 3, 4], 2) ➞ True
# Two groups of length 2: [3, 4], [5, 6]

consecutive_nums([1, 3, 4, 5], 2) ➞ False
# It is possible to make one group of length 2, but not a second one.

consecutive_nums([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) ➞ True
# [1, 2, 3], [2, 3, 4], [6, 7, 8]

consecutive_nums([1, 2, 3, 4, 5], 4) ➞ False
# The list length is not divisible by the group’s length.
"""

def consecutive_nums(lst, group_len):
    #sort list
    lst.sort()
    if list and group_len == 1:
        return True
    elif list and group_len and len(lst) % group_len == 0:
        #iterate through list
        for i in range(0, len(lst), group_len):
            #check if consecutive
            if lst[i] != lst[i+1] - 1:
                return False
            elif lst[i] == lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i+2]
                lst[i+2] = temp
                
        return True
    return False


print(consecutive_nums([1, 3, 5], 1), True)
print(consecutive_nums([1, 2, 3, 3, 3, 3], 3), False)
print(consecutive_nums([5, 6, 3, 4], 2), True)
print(consecutive_nums([1, 3, 4, 5], 2), False)
print(consecutive_nums([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True)
print(consecutive_nums([1, 2, 3, 4, 5], 4), False)
print(consecutive_nums([6, 6, 6, 9, 7, 8, 7, 5, 8, 5, 7, 8], 4), True)
print(consecutive_nums([3, 9, 2, 2, 7, 6, 5, 8, 5, 2, 7, 4, 5, 3, 4, 4, 6, 2, 3, 4], 4), False)
print(consecutive_nums([3, 4, 1, 2, 3, 2, 3, 4, 5], 3), True)
print(consecutive_nums([9, 9, 7, 3, 3, 1, 1, 1, 2, 8, 8, 7, 2, 2, 3], 3), True)
print(consecutive_nums([5, 5, 7, 3, 3, 1, 1, 1, 2, 6, 6, 7, 2, 2, 3], 3), True)