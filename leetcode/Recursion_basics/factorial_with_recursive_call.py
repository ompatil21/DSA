"""
find factorial of N
"""


def factorial(n):
    # Base case: 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)


print(factorial(5))  # Output: 120


# without recusion
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by the current number
    return result


print(factorial(5))  # Output: 120
