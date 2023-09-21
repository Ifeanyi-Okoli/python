""" 
Array Challenge
Have the function ArrayChallenge(arr) take the array of integers stored in arr, and find the four largest elements and return their sum. For example: if arr is [4, 5, -2, 3, 1, 2, 6, 6] then the four largest elements in this array are 6, 6, 4, and 5 and the total sum of these numbers is 21, so your program should return 21. If there are less than four numbers in the array your program should return the sum of all the numbers in the array.
Examples
Input: [1, 1, 1, -5]
Output: -2
"""








input = [1, 1, 1, -5]




def ArrayChallenge(arr):
    #sort in descending order
    if len(arr) < 4:
        return sum(arr)
    arr.sort(reverse=True)
    #return sum of first 4 elements
    return sum(arr[:4])
    


# keep this function call here 
print(ArrayChallenge(input))
print(ArrayChallenge([0, 0, 2, 3, 7, 1]))
print(ArrayChallenge([7, 1]))
