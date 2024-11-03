""" print start to end"""


def stoe(start, end):

    while start <= end:
        print(start, end=" ")
        start += 1
    print()


stoe(11, 20)


"""
print this pattern 
1 8 15 22 29 36 43 50 57 64 71 78 85 92 99
"""
i = 1
while i < 105:
    print(i, end=" ")
    i += 7
print()


"""print all the odd numbers less than 15"""

num = 1
while num < 15:
    print(num, end=" ")
    num += 2
print()


"""calculate factorial of given number """

number = 3
factorial = 1

while number > 0:
    factorial *= number  # Multiply factorial by the current number
    number -= 1  # Decrement number by 1

print(factorial)


""" print all the number divisible by 3 and 5 between n1 to n2"""


def divby_3_and_5(n1, n2):
    while n1 <= n2:
        # Check if n1 is divisible by both 3 and 5
        if n1 % 3 == 0 and n1 % 5 == 0:
            print(n1)
        # Increment n1 to check the next number
        n1 += 1


print()

# Example call
divby_3_and_5(10, 30)


"""crete a function named calsum which takes two arguments 
    calculate sum of all numbers from n1 to n2
"""


def calsum(n1, n2):
    if n1 > n2:
        return "n1 should be smaller than n2"
    sum = 0
    while n1 <= n2:
        sum = sum + n1
        n1 += 1
    return sum


print(calsum(5, 9))
