"""
find  the length of list without using len function
"""

my_list = [12, 1, 2, 32, 434, 35, "gfgfg", "egergergdv"]
count = 0
for i in my_list:
    if i != None:
        count += 1
print(count)


"""
print the list in reverse order using while loop and for loop
"""

n = len(my_list)

for i in range(n - 1, 0, -1):
    print(my_list[i], end=" ")


while i < n:
    print(my_list[i], end=" ")
    i += 1


print()
"""
make a list of your own and print all the numbers which are divisible by 3 and 4 in the list 
"""

number_list = [11, 22, 4, 442, 4354, 56, 676, 5, 7688, 234, 12, 55, 245]

for i in number_list:
    if i % 3 == 0 and i % 4 == 0:
        print(i)


print()
"""
Make a list of your own and count how many numbers are divisible by 5 in the list
"""

divisible_by5 = 0
for i in number_list:
    if i % 5 == 0:
        divisible_by5 += 1

print(divisible_by5)


print()
"""
create a function CountOddEven that accepts an list integers and print how mant odd and even numbers are there
"""


def CountOddEven(intlist):
    OddCount = 0
    EvenCount = 0
    for i in intlist:
        if i % 2 == 0:
            EvenCount += 1
        else:
            OddCount += 1

    return f"Count of Odd numbers in the given list is: {OddCount}, Count of Even numbers in the list is: {EvenCount}"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = CountOddEven(numbers)
print(result)


print()
"""
create a function to SumCountOddEven that accepts an list of integers and calculate sum of odd and even numbers 
"""


def SumCountOddEven(numbers):
    OddCountSum = 0
    EvenCountSum = 0
    for i in numbers:
        if i % 2 == 0:
            EvenCountSum += i
        else:
            OddCountSum += i

    return f"Sum of all Even numbers in the list is {EvenCountSum} and sum of all Odd numbers in the list is {OddCountSum}"


OddEvenSum = SumCountOddEven(numbers)
print(OddEvenSum)


print()
"""
create a function FindLargest which accepts list integers and returns the largest number from the list 
"""


def FindLargest(numbers):
    Largest = numbers[0]
    for i in numbers:
        if i > Largest:
            Largest = i
    return Largest


print(FindLargest(numbers))


print()

"""
create a function FindSmallest which accepts an list of integers and return the smallest number
"""


def FindSmallest(numbers):
    Smallest = numbers[0]
    for i in numbers:
        if Smallest > i:
            Smallest = i
    return Smallest


print(FindSmallest(numbers))
