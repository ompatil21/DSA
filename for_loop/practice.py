"""create a function divs which takes two integers as parameter n1,n2 and 
return how many number are divisible by n2 in between 1 to n1"""


def divs(n1, n2):
    number = 0
    for i in range(1, n1 + 1):
        if i % n2 == 0:
            number += 1
    return number


print(divs(8, 2))


"factorial function"


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(factorial(5))


def pattern1(n1):
    for i in range(1, 8):
        print(i * 4, end=" ")


pattern1(4)


num1 = int(input("Enter a number for pattern printing: "))
for i in range(1, num1, 10):
    num = 1
    num = i * 10 + num
    print(num)


"""2 22 222 2222 22222 pattern"""


def pattern(n: int) -> None:
    i: int = 1
    num: int = 2
    while i <= n:
        print(num, end=" ")
        num = (num * 10) + 2
        i += 1
    print()


pattern(5)


"""harmonic series pattern"""


def harmonicseries(n):
    if n < 1:
        print("please enter a positive number")

    total = 0.0
    i = 1
    while i <= n:
        total += 1 / i
        i += 1
    return total


print(harmonicseries(5))


def pattern3(x, n):
    i = 1
    total = 0
    y = 1
    while i <= n:
        total += x / y
        y += 2
        i += 1
    return total


print(pattern3(6, 4))
