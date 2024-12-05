"""
Write a Python program to find repeated items in a tuple.
"""


def find_repeated_items(tpl):
    repeated_items = []
    for item in tpl:
        if tpl.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items


my_tuple = (1, 2, 3, 4, 5, 2, 3, 6, 7, 3, 4, 4)
repeated = find_repeated_items(my_tuple)
print("Repeated items:", repeated)


"""
Write a Python program to check whether an element exists within a tuple. 
Ask something from user, if that exists in tuple, then print “YES” else print “NO”.
"""


def elementExistsInTuple(element, t):
    return element in t


my_tuple = (1, 2, 3, 4, 5)

e = int(input("Enter an element = "))

if elementExistsInTuple(e, my_tuple):
    print("YES")
else:
    print("NO")


"""
Write a Python program to reverse a tuple.
"""


def reverse_tuple(tpl):
    return tpl[::-1]


my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = reverse_tuple(my_tuple)
print("Original Tuple:", my_tuple)
print("Reversed Tuple:", reversed_tuple)


"""
Write a Python program to check if a string has at least one letter and one number. 
If it has at least one letter and one number then print YES else print NO.
"""


def checkNumberAndLetter(my_string: str) -> bool:
    isLetter = False
    isNumber = False

    # Method 1
    """
    for ch in my_string:
        if ch.isdigit():
            isNumber = True
        elif ch.isalpha():
            isLetter = True

    return isLetter and isNumber
    """

    for ch in my_string:
        ascii_code = ord(ch)
        if ascii_code >= 48 and ascii_code <= 57:
            isNumber = True
        elif (ascii_code >= 65 and ascii_code <= 90) or (
            ascii_code >= 97 or ascii_code <= 122
        ):
            isLetter = True

    return isLetter and isNumber


print(checkNumberAndLetter("abc#$#1d"))


"""
Write a python program to ask a string from user. 
Then count the number of vowels and number of consonants in that string.
"""


def count_vowels_and_consonants(string: str):
    vowels = 0
    consonants = 0
    new_string = string.lower()  # Convert to lowercase

    for ch in new_string:
        if ch.isalpha():
            if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants
