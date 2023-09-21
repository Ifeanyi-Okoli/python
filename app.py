print("Hello, World!")

def countdown(start):
    print(start)
    if start > 0:
        # print(start)
        countdown(start - 1)
        
countdown(5)


def sum(n):
    total=0
    for i in range(n-1):
        total += i
    return total

result = sum(100)
print (result)