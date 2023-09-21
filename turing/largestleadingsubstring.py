""" 
Largest leading substring
You are given a non-empty array of strings. Write a function to find the largest set of characters that are shared between all of them. The longest should be able to handle cases where there are no common preceding characters among the strings provided. Additionally, the algorithm should be optimized for efficiency and avoid using any built-in functions.

"""

def leadingsubstring(s):
    #sort list
    s.sort()
    #get first and last word
    first = s[0]
    last = s[-1]
    #iterate through first word
    for i in range(len(first)):
        #compare first and last word
        if first[i] != last[i]:
            return first[:i]
    return first

print(leadingsubstring(['flower', 'flow', 'flight']), 'fl')
