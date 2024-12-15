"""
write python function which counts number of digits given in a string using ascii code
"""


def digits(a):
    count = 0
    for ch in a:
        ascii_code = ord(ch)
        if (
            48 <= ascii_code <= 57
        ):  # Check if the character's ASCII code is within the digit range
            count += 1
    return count


a = "ROOM 101"
print("Number of digits in the string:", digits(a))


"""
write a python script counts how many letter are in a string by checking ascii values
"""


def letters(string):
    letter = 0
    for ch in string:
        ascii_code = ord(ch)
        if 65 <= ascii_code <= 90 or 97 <= ascii_code <= 122:
            letter += 1

    return letter


string = "Year 2022!"
print("Number of letters in the string:", letters(string))


"""
write a function which checks if the string is alphanumeric 
"""


def alphanumeric(s):
    for ch in s:
        ascii_code = ord(ch)
        # If any character is not alphanumeric, return False
        if not (
            65 <= ascii_code <= 90 or 97 <= ascii_code <= 122 or 48 <= ascii_code <= 57
        ):
            return False
    return True  # If all characters are alphanumeric, return True


s = "njnjASADAfnen343413413"
print("Is string alphanumeric :", alphanumeric(s))


"""
write a function which toggles the case of letter in a string 
"""


def toggles(s):
    toggled_string = ""
    for ch in s:
        ascii_code = ord(ch)
        if 65 <= ascii_code <= 90:  # Uppercase letter
            toggled_string += chr(ascii_code + 32)  # Convert to lowercase
        elif 97 <= ascii_code <= 122:  # Lowercase letter
            toggled_string += chr(ascii_code - 32)  # Convert to uppercase
        else:
            toggled_string += ch  # Non-alphabetical characters remain the same
    return toggled_string


input_string = "Hello World! 123"
print("Original String:", input_string)
print("Toggled String:", toggles(input_string))


"""
write a program that converts each non alphabetic charecter in a string with a space using ascii 
"""


def replace_non_alphabetic_with_space(s):
    result = ""
    for ch in s:
        ascii_code = ord(ch)
        # Check if the character is alphabetic (A-Z or a-z)
        if 65 <= ascii_code <= 90 or 97 <= ascii_code <= 122:
            result += ch  # Keep the alphabetic character
        else:
            result += " "  # Replace non-alphabetic character with a space
    return result


input_string = "Hello! How are you doing? #2024"
output_string = replace_non_alphabetic_with_space(input_string)

print("Original String:", input_string)
print("Modified String:", output_string)


""""
write a programme to calculate sum of ascii code of all the cherecter in a string 
"""


def sumAscii(S):
    Ascii_character_sum = 0
    for ch in S:
        Ascii_character_sum += ord(ch)  # Add ASCII value of each character
    return Ascii_character_sum


# Test the function
S = "ISDOIU3232"
print("Sum of ASCII characters in the string:", sumAscii(S))
