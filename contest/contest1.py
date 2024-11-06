"""
create a function that takes an integer as an argument and checks if the number is prime or not 
"""


def checkPrime(num):
    if num < 2:
        return "Given number is not a prime number"
    elif num == 2:
        return "Given number is a prime number"

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Given number is not a prime number"

    return "Given number is a prime number"


print(checkPrime(22))


"""
Print all the prime number from 1 to 100
"""


def print_primes():
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")


print_primes()


"""
create a function named sumNum() which takes two parameters n1 and n2
calculate and return sum of all the numbers which are divisible by 2 and 7 
between n1 and n2 also if the sum is 0 then return -1
"""


def sumNum(n1, n2):
    total = 0
    for num in range(n1, n2):
        if num % 2 == 0 and num % 7 == 0:
            total += num

    return total if total != 0 else -1


print()
print(sumNum(1, 30))


"""
create a function named factorial which takes num as paramter and returns the factorial of that number 
"""


def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        i = 2
        while i <= num:
            result *= i
            i += 1
        return result


print(factorial(5))


"""
create a function named sumPattern() which takes integer n as argument and calculate the sum of following pattern 
sumpattern(3)
1/1! + 1/2! + 1/3!

"""


def sumPattern(num):
    if num == 0:
        return 0
    else:
        patternSum = 0.0
        result = 1

        for i in range(1, num + 1):
            if i == 1:
                result = 1
            else:
                result *= i  #

            patternSum += 1 / result

        return patternSum


print(sumPattern(5))


"""
create a function named sum of squares which takes single integer n as parameter return sum of squares from 1 to n
"""


def sumofSqures(n):
    result = 0
    for i in range(1, n + 1):
        result = (i**2) + result
    return result


print(sumofSqures(5))


"""
create a function named PrintPrimeFactor that takes an integer n as an argument print all the prime factors of that number
"""


def PrintPrimeFactor(n):
    if n < 1:
        print("Given number is negative or zero")
        return

    while n % 2 == 0:
        print(2, end=" ")
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            print(i, end=" ")
            n = n // i

    if n > 2:
        print(n, end=" ")


PrintPrimeFactor(10)
