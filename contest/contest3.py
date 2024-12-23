"" """
Given a list of strings concanate them into a single line seperated by spaces and dont use join funtions
"""

Example = ["Hello", "World"]


def concanate(strings: list) -> str:
    new_string = ""
    for i in strings:
        if new_string:  # If new_string is not empty, add a space
            new_string += " "
        new_string += i
    return new_string


print(concanate(Example))


"""
write a programme to rotate the charecter in a string by a given number of positions 
for example the given input is "abcdef" and the rotation of 2 output should be "efabcd"
ask string and rotation from the user 
"""


def rotate_string():
    # Get input from the user
    string = input("Enter the string to rotate: ")
    rotation = int(input("Enter the number of positions to rotate: "))

    # Ensure the rotation is within the length of the string
    rotation = rotation % len(string)

    # Perform the rotation
    rotated_string = string[-rotation:] + string[:-rotation]

    return rotated_string


# Call the function and display the result
result = rotate_string()
print("Rotated string:", result)


"""
write a python programme to convert all the charecters of a string to uppercase
if the two charecters of the string are capital among the first four charecters  
"""


def capitalize(strings: str) -> str:
    # Count the number of uppercase letters in the first 4 characters
    capital_count = sum(1 for chr in strings[:4] if "A" <= chr <= "Z")

    if capital_count >= 2:
        # Convert the entire string to uppercase if condition is met
        return strings.upper()
    else:
        # Return a message if condition isn't met
        return "Not enough capital characters in the first four letters."


print(capitalize("PyThon"))


"""
create a dictionary that count the frequency of words in a string
"""


def wordFrequency(string: str):
    words = string.split()
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict


frequency = wordFrequency("hey there its me om ! hey")
print(frequency)


"""
write a function to map two lists into a dictionary every element should be unique in the
dictionary
"""


def listsToDictionary2(list1: list, list2: list) -> dict | str:
    if len(list1) != len(list2):
        return "Length of List must be the same"

    output_dict = {}
    for i in range(len(list1)):
        output_dict[list1[i]] = list2[i]
    return output_dict


list1 = ["red", "green", "blue"]
list2 = ["#FF0000", "#008000", "#0000FF"]

output_dict = listsToDictionary2(list1, list2)
print(output_dict)


"""
converting string values in dictionaries within a list to either integers or floats
based on whether the value contains a decimal point
"""


def convertValues(data: list[dict]):
    for d in data:
        for key, value in d.items():
            if "." in value:
                d[key] = float(value)
            else:
                d[key] = int(value)
    return data


list2 = [
    {"x": "10.12", "y": "20.23", "z": "30"},
    {"p": "40.00", "q": "50.19", "r": "60.99"},
]

output2 = convertValues(list2)
print(output2)
