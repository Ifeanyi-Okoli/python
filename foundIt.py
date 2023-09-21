import random


def found_it(nums, looking_for):
    for i, x in enumerate(nums):
        if x == looking_for:
            return True


nums = [x for x in range(1000)]
looking_for = 500
print(found_it(nums, looking_for))

""" 
The function's purpose is to search for the looking_for number within the nums list. It does so by iterating through the nums list using a for loop and enumerate to track the index (position) and value of each element in the list. If it finds an element in the nums list that is equal to the looking_for value (in this case, 500), it immediately returns True, indicating that it has found the number. If it completes the loop without finding the desired number, it implicitly returns None (Python's default return value).

In the provided code, the nums list contains numbers from 0 to 999, and looking_for is set to 500. The code then calls the found_it function with these values and prints the result. If 500 is present in the nums list, it will print True, indicating that it has found the number; otherwise, it will print None.
"""


def fine_tune_model(iterations, cut_off, *engg, **grid_search):
    for i in range(iterations):
        for key, value in grid_search.items():
            print(key, value)
        print(cut_off)
        print(engg)


l = [1, 2, 3, 4, 5]
# print(l**2)
print(map(lambda x: x**2, l))
# print(map(x: x**2, l))
# print(map(l, lambda x: x**2))

# for i in range(n//2, n):
#     for j in range(1, (n//2)+1):
#         for k in range(2, n, pow(2,k)):
#             print(i, j, k)


# numbers = [num for num in range(0, 100)]
# shuffled = random.shuffle(numbers)
# pick = random.choice(shuffled)

document = (2020, 'Python', 'Java', 'C++',
            ['Machine Learning', 'Deep Learning'])
document[-1].append('NLP')
print(document)