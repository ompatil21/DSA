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
