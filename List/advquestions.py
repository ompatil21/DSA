"""
given a number return list containing the two halves of number if the number is odd make the rightmost number larger 

"""


def TwoHalves(n):
    temp = []
    FirstHalve = n // 2
    SecondHalve = n - FirstHalve

    return [FirstHalve, SecondHalve]


print(TwoHalves(15))


print()
"""
list can be mixed with various types.Your task for this challenge is to sum all the elements in the list create a function
that takes a list and returns the sum of all numbers in the list 

"""


def sum_numbers(mixed_list):
    total = 0
    for item in mixed_list:
        if isinstance(item, (int, float)):
            total += item
    return total


mixed_list = [1, "hello", 3.5, [2, 3], 10, "world", 7]
print(sum_numbers(mixed_list))


"""
create a function that takes list of integers as the parameter and returns the unique number from the list  
"""


def find_unique(numbers):

    for num in numbers:
        if numbers.count(num) == 1:
            return num
    return None


numbers = [1, 2, 3, 4, 2, 3, 4]
print(find_unique(numbers))
