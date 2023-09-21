""" 
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
"""

def permutations(s):
    # Code Away!
    arr = []
    if len(s) == 1:
        return [s]
    for i in range(len(s)):
        print(s[:i])
        # print(s[i+1:])
        for perm in permutations(s[:i] + s[i+1:]):
            arr.append(s[i] + perm)
    return list(set(arr))
    

# print(sorted(permutations('a')), ['a']);
# print(sorted(permutations('ab')), ['ab', 'ba'])
print(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])