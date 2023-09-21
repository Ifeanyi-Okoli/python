""" 
Valid Substrings
Given a string of k of lower-case letters, the letters can be repeatedand exist consecutively.
A substring from k is considered valid if it contains at least 3 consecutive identical letters
return indices of the valid substrings of a given string k. Must order the pairs by the start index  in ascending order.
"""

# def solution(k):
#     # Your code here
#     result = []
#     for i in range(len(k)-2):
#         if k[i] == k[i+1] and k[i] == k[i+2]:
#             result.append([i, i+2])
#     return result

def solution(k):
    result = []
    i = 0
    while i < len(k):
        count = 1
        j = i + 1
        while j < len(k) and k[j] == k[i]:
            count += 1
            j += 1
        if count >= 3:
            result.append([i, j - 1])
        i = j
    return result

print(solution("aabbbcc"))
print(solution("aabbbccaa"))
print(solution("abcdddeeeeaabbbcd"))