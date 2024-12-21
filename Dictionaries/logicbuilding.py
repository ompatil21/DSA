"""
write a function that takes a dictionary and a key and return True if the key 
is found or else returns False 
"""


def key_check(Dict, key):
    for k in Dict.keys():  # Loop through the keys of the dictionary
        if k == key:  # Check if the key matches
            return True
    return False


test_dict = {"a": 1, "b": 2, "c": 3}

print(key_check(test_dict, "a"))  # True (key exists)
print(key_check(test_dict, "z"))  # False (key does not exist)


"""
write a function to merge two dictionaries if there is overlap of keys 
then value of the second dictionary should overwrite 
"""


# Method 1
def merge_dictionaries(d1, d2):
    merged = d1.copy()  # Copy the first dictionary
    merged.update(d2)  # Update with the second dictionary (overwrites if key exists)
    return merged


# Method 2
def merge_dictionaries2(d1, d2):
    merged = d1.copy()  # Start with a copy of the first dictionary
    for key, value in d2.items():
        merged[key] = (
            value  # Set the value from the second dictionary, overwriting if key exists
        )
    return merged


print(
    merge_dictionaries2(
        {"apple": 3, "banana": 5, "cherry": 7},
        {"banana": 8, "orange": 10, "apple": 9},
    )
)
