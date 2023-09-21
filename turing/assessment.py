""" 
Number Genrator
A digit-only keyboard contains all 10 digits from 0 yo 9. They all in one line.
Given a string of 10 digits illustrating how the keys are positioned. To type a digit, you start from
indes zero to the index of the target digit. it takes a - b jmillisecosd to move from a to index b.
write a function to calculate the number of millisecods needed to type a number with one finger.
"""

def numMiliiseconds(keyboard, target):
    timeelapsed = 0
    currentIndex = 0
    for i in range(len(target)):
        if target[i] == keyboard[currentIndex]:
            continue
        else:
            timeelapsed += abs(keyboard.index(target[i]) - currentIndex)
            currentIndex = keyboard.index(target[i])
    return timeelapsed
    

print(numMiliiseconds("0123456789", "0123456789"), 0)
print(numMiliiseconds("0876543210", "1234567890"), 9000)
print(numMiliiseconds("0123456789", "210"), 210)