"""
create a function which takes a string as a argument and returns the list
of charecters which appears odd number of times 
"""


def oddCharacters(string: str) -> list:
    # Dictionary to store the frequency of each character
    char_count = dict()

    # Count the frequency of each character
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Collect characters that appear an odd number of times
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]

    return odd_chars


string = input("Enter a string: ")
print(f"Charecters that appear odd number of times{oddCharacters(string)}")


"""
Given string S contains numeric word , task is to convert the word into the actual words
"""


def wordToNum(s):
    # Mapping of words to numbers
    word_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }

    # Splitting the string into words
    words = s.split()

    # Converting words to numbers
    frequency_list = [word_to_num[word] for word in words if word in word_to_num]

    return frequency_list


print(wordToNum("one two three "))


"""
snake_Case to Pascal_case
"""


def snake_to_pascal(snake_str: str) -> str:
    # Split the string by underscores
    words = snake_str.split("_")

    # Initialize an empty string for the result
    pascal_case = ""

    # Loop through each word, capitalize it, and add it to the result
    for word in words:
        pascal_case += word.capitalize()

    return pascal_case


print(snake_to_pascal("this_is_snake_case"))
print(snake_to_pascal("convert_to_pascal"))


"""
create a function to captilize the firtst and last letter of a word in a string 
"""


def capitalize_first_and_last(word: str) -> str:
    if len(word) > 1:
        # Capitalize the first and last letters, keep the middle part as is
        return word[0].upper() + word[1:-1] + word[-1].upper()
    elif len(word) == 1:
        # If the word is a single letter, just capitalize it
        return word.upper()
    else:
        # Return the word as is if it's empty
        return word


def capitalize_first_and_last_in_string(s: str) -> str:
    # Split the string into words
    words = s.split()

    # Process each word and capitalize the first and last letter
    capitalized_words = [capitalize_first_and_last(word) for word in words]

    # Manually concatenate the words with spaces
    result = ""
    for i, word in enumerate(capitalized_words):
        if i == 0:
            result += word
        else:
            result += " " + word

    return result


print(capitalize_first_and_last_in_string("hello world"))
print(capitalize_first_and_last_in_string("a b c"))


"""
create a fucntion in which we can create two strings from a single string 
first string should have all the charecters that appear only once and 
second string should have charecters that appear multiple times
"""


def separate_chars(s: str):
    # Create a dictionary to store frequency of each character
    char_count = {}

    # Count the frequency of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Initialize two strings: one for unique chars, one for multiple chars
    unique_chars = ""
    multiple_chars = ""

    # Loop through the frequency dictionary
    for char, count in char_count.items():
        if count == 1:
            unique_chars += char
        elif count > 1:
            multiple_chars += char

    return unique_chars, multiple_chars


unique, multiple = separate_chars("programming")
print(f"Unique characters: {unique}")
print(f"Multiple characters: {multiple}")
