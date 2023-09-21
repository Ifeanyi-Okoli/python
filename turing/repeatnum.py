""" 
Suppose you are given a set which originally contains numbers from 1 to n. For some reason, one of the numbers in the set is removed and replaced with a duplicate of another number in the set. Find and return the duplicate number.
given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
"""

# def repeatandmissingnum(arr):
#     #sort array
#     arr.sort()
#     #iterate through array
#     for i in range(len(arr)-1):
#         #check if consecutive
#         if arr[i] == arr[i+1]:
#             return [arr[i], i+2]
#     return None


def repeatandmissingnum(arr):
    n = len(arr)
    #find sum of array
    sum_arr = sum(arr)  
    #find sum of n numbers
    sum_n = (n*(n+1))//2
    #find sum of squares of array
    sum_sq_arr = sum([x*x for x in arr])
    #find sum of squares of n numbers
    sum_sq_n = (n*(n+1)*(2*n+1))//6
    #find difference
    diff = sum_n - sum_arr
    #find sum of squares difference 
    sum_sq_diff = sum_sq_n - sum_sq_arr
    #find sum of missing and repeat number
    sum_missing_repeat = sum_sq_diff//diff
    #find missing number
    missing = (sum_missing_repeat + diff)//2
    #find repeat number
    repeat = sum_missing_repeat - missing
    return [repeat, missing]

print(repeatandmissingnum([1,2,2,4]))
print(repeatandmissingnum([1,3,3]))
print(repeatandmissingnum([2,2,3,4]))