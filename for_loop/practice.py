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


def pattern(n1):
    for i in range(1, 8):
        print(i * 4, end=" ")


pattern(4)


num1 = int(input("Enter a number for pattern printing: "))
for i in range(1, num1, 10):
    num = 1
    num = i * 10 + num
    print(num)
