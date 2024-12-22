"""
Write a Python script to sort (ascending and descending) a dictionary by value.
Sample Outputdictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Ascending order = { 0:0, 2:1, 1: 2, 3: 4}
Descending order = {3: 4, 4: 3, 1: 2, 2: 1, 0: 0
"""

# Sample dictionary
dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Sorting in ascending order by value
ascending_order = dict(sorted(dictionary.items(), key=lambda item: item[1]))

# Sorting in descending order by value
descending_order = dict(
    sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
)

# Display the results
print("Original dictionary:", dictionary)
print("Ascending order:", ascending_order)
print("Descending order:", descending_order)


"""
write a function to count number items in value of a dictionary
"""


def dictValueCount(dict1):
    count = 0
    for value in dict1.values():
        if isinstance(
            value, (list, tuple, set, dict)
        ):  # Check if the value is a collection
            count += len(value)  # Add the number of items in the value
        else:
            count += 1  # Count non-iterable values as 1
    return count


# Example usage
dictionary = {
    1: [1, 2, 3],
    2: "hello",  # Counted as 1 (non-iterable string)
    3: {1: "a", 2: "b"},  # Nested dictionary
    4: (10, 20),  # Tuple
    5: {10, 20, 30},  # Set
}

print(dictValueCount(dictionary))  # Output: 11


# method 2


def countItems(dict1):
    count = 0
    for k, v in dict1.items():
        count += len(v)
    return count


result = countItems({"M1": [67, 79, 90, 73, 36], "M2": [89, 67, 84], "M3": [82, 57]})
print(result)


"""
write a python programme to print dictionary line by line
"""
# Sample dictionary
Dict = {"Sam": {"M1": 89, "M2": 56, "M3": 89}, "Suresh": {"M1": 49, "M2": 96, "M3": 89}}


# Function to print the dictionary line by line
def print_dict_line_by_line(d):
    for key, value in d.items():
        print(key)  # Print the outer dictionary key
        if isinstance(value, dict):  # Check if the value is a nested dictionary
            for sub_key, sub_value in value.items():
                print(f"{sub_key} : {sub_value}")  # Print nested key-value pairs
        else:
            print(f"Value : {value}")  # Print the value if it's not a dictionary


# Call the function
print_dict_line_by_line(Dict)


"""
write a python programme to convert a two lists into one dictionary
"""


def convertToDictionary(lst1, lst2):
    dictionary = {}
    for i in range(len(lst1)):
        # dictionary.update({lst1[i]: lst2[i]})
        dictionary[lst1[i]] = lst2[i]
    return dictionary


keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
my_dict = convertToDictionary(keys, values)
print(my_dict)


"""
create a python function to sort the dictionary by its values and return a new dictionary
"""
Dict = {"Sam": 892, "Suresh": 891}


def sortDictionary(dictionary):
    return dict(sorted(Dict.items(), key=lambda x: x[1]))


print(f"Ascending order = {sortDictionary(Dict)}")
