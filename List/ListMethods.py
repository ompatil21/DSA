"""
make empty list named odd and even and add the the odd numbers to odd list and all the even numbers to even list 
"""

numberList = [52, 43, 87, 14, 85, 41, 26, 60, 52, 55, 90, 94, 82, 87, 50]


def oddEven(lst):
    odd = []
    even = []
    for i in lst:
        if i % 2 == 0:  # Check if the number is even
            even.append(i)
        else:  # Otherwise, it is odd
            odd.append(i)
    return odd, even


# Example usage
odd_numbers, even_numbers = oddEven(numberList)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)


"""
write a function to remove all the duplicates from the list and print them
"""


def find_and_remove_duplicates(lst):
    unique_elements = []
    duplicates = []

    for i in lst:
        is_duplicate = False
        # Check if the element already exists in unique_elements
        for j in unique_elements:
            if i == j:
                is_duplicate = True
                break

        if is_duplicate:
            # Check if the duplicate is already in duplicates list
            already_added = False
            for k in duplicates:
                if i == k:
                    already_added = True
                    break
            if not already_added:
                duplicates.append(i)
        else:
            unique_elements.append(i)

    return unique_elements, duplicates


# Example usage
unique_numbers, duplicate_numbers = find_and_remove_duplicates(numberList)

print("Unique elements:", unique_numbers)
print("Duplicate elements:", duplicate_numbers)


def CommonElement(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:  # Check if any element in l1 is present in l2
                return True
    return False


# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 2, 10]
print(CommonElement(list1, list2))  # Output: True


"""
write a funtion that finds sum and average of list  
"""


def sum_and_average(lst):
    total_sum = 0
    count = 0

    for num in lst:
        total_sum += num  # Add each number to total_sum
        count += 1  # Increment the count of numbers

    average = total_sum / count if count != 0 else 0  # Avoid division by zero
    return total_sum, average


# Example usage
numbers = [1, 2, 3, 4, 5]
total, avg = sum_and_average(numbers)
print(f"Sum: {total}, Average: {avg}")


"""
write a function which take all the common elements from the two list and returns and new list of all the common elements

"""


def Common(lst1, lst2):
    lst3 = []
    for i in lst1:
        for j in lst2:
            if i == j:  # Check if an element in lst1 matches an element in lst2
                if i not in lst3:  # Avoid duplicate entries in the result
                    lst3.append(i)
    return lst3


# Example usage
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [11, 22, 331, 2, 3]
print(Common(numbers1, numbers2))


"""
write a function to remove Nth index from the list 
"""


def removeNth(lst, n) -> None:
    if n < 0 or n >= len(lst):
        print("Index out of range")
        return
    lst.pop(n)


# Example usage
numbers = [10, 20, 30, 40, 50]
index_to_remove = 2
removeNth(numbers, index_to_remove)
print(numbers)  # Output: [10, 20, 40, 50]


"""
make two list of same length and pass it to a fuction return a third list where each element is sum of elements
"""


def SumElement(l1, l2):
    if len(l1) == len(l2):
        l3 = []  # Initialize an empty list for the result
        for i in range(len(l1)):
            l3.append(l1[i] + l2[i])  # Add corresponding elements and append to l3
        return l3
    else:
        return "The lengths of the two lists do not match."


# Example usage
numbers1 = [10, 20, 30, 40, 50]
numbers2 = [1, 2, 3, 4, 5]
print(SumElement(numbers1, numbers2))  # Output: [11, 22, 33, 44, 55]


"""
Take ten inputs from the user and add it to the list and now copy all the elements in the new list in reverse order 
"""


def reverse_list():
    # Take ten inputs from the user
    original_list = []
    print("Enter 10 numbers:")
    for _ in range(10):
        number = int(input())
        original_list.append(number)

    # Create a new list with elements in reverse order
    reversed_list = []
    for i in range(len(original_list) - 1, -1, -1):
        reversed_list.append(original_list[i])

    return original_list, reversed_list


# Example usage
original, reversed_lst = reverse_list()
print("Original List:", original)
print("Reversed List:", reversed_lst)
