"""
Make a dictionary with subjects 'maths','science','english' and print the subject with highest number of marks
"""

subjects = {
    "Math": 94,
    "English": 99,
    "Science": 93,
}
highest = 0

for i in subjects.values():
    if i > highest:
        highest = i

print(highest)


"""
Make a dictionary with subjects and print the subject name with highest number of marks
"""


subject_marks = {
    "physics": 67,
    "chemistry": 12,
    "english": 95,
    "computer": 99,
    "hindi": 54,
}

highest = 0
highest_subject = ""
for subject, mark in subject_marks.items():
    if mark > highest:
        highest = mark
        highest_subject = subject

print(f"Highest marks scored is {highest} in {highest_subject} subject")


"""
Make a dictionary with subjects 'maths','science','english' and print the subjects name with marks below 35
"""
subject_marks1 = {
    "physics": 67,
    "chemistry": 12,
    "english": 95,
    "computer": 99,
    "hindi": 54,
}

marks = 0
subject = ""

for subject, marks in subject_marks1.items():
    if marks < 35:
        print(subject, marks)


""""
write a python programme to generate and print dictionary that contains a number between 1 to n 
in the form of (x,x*x) 
"""


def createDictionary(n):
    my_dict = {}
    for i in range(1, n + 1):
        my_dict[i] = i**2
    return my_dict


print(createDictionary(5))


"""
write a python programme to check if the dictionary is empty or not
"""


def isEmpty(dictionary):
    # Method 1 (Best way)
    """
    if not dictionary:
        return True
    return False
    """

    # Method 2
    """
    if len(dictionary.keys()) == 0:
        return True
    return False
    """

    # Method 3
    count = 0
    for i in dictionary.keys():
        count += 1
    if count == 0:
        return True
    return False


print(isEmpty({}))
print(isEmpty({"name": "om"}))


"""
write a python prgramme to find the size of dictionary that number of key and value pairs
"""


def dict_size(dictionary):
    return len(dictionary.keys())


print(dict_size({}))
print(dict_size({"name": "om"}))
