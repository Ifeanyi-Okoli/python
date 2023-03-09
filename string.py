"""_summary_
    Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
    """


def repeat_string(n, s):
    return s * n


def main():
    print(repeat_string(6, "I"))
    print(repeat_string(5, "Hello"))
