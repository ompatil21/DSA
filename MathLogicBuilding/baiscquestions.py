# QI. Write a Python function to find the Maximum and minimum of three
# numbers. Use 3 parameters. Make 2 different functions named as maxi and
# mini.


def maxi(a, b, c):
    if a > b and a > c:
        print("a is the gratest")
    elif b > a and b > c:
        print("b is the greatest")
    elif c > a and c > b:
        print("c is the greatest")


maxi(99, 128, 336)


def greet_name(name):
    print(f"hey there how are you {name}")


greet_name("om")


def simple_calculator(a, b, operation):
    if operation == "add":
        print(a + b)
    else:
        print(a - b)


simple_calculator(10, 20, "add")


def check_number(number):
    if number == 0:
        print("number is zero")
    elif number < 0:
        print("negative number")
    else:
        print("positve number")


check_number(0)


def odd_even(num):
    if (num // 2) * 2 == num:
        print("even number")
    else:
        print("odd number")


odd_even(13)


def largestNum(a=None, b=None, c=None):
    if a == None and b == None and c == None:
        return -1

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


print(largestNum(11, 4, 2))


def baseExpo(base, exponent):
    return base**exponent


print(baseExpo(2, 3))


def middlecheck(a, b, c):
    # Find the middle number among three numbers
    if (a < b < c) or (c < b < a):
        return b
    elif (b < a < c) or (c < a < b):
        return a
    else:
        return c


print(middlecheck(111, 331, 22))
