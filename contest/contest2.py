"""
create a function named isPalindrome which accepts a string as a parameter and returns True 
if its a palindrome
"""


def isPalindrome(s):
    # Convert to lowercase manually
    lowercase_s = ""
    for ch in s:
        if 65 <= ord(ch) <= 90:  # Convert uppercase letters to lowercase
            lowercase_s += chr(ord(ch) + 32)
        else:
            lowercase_s += ch

    # Check if the string is a palindrome by comparing characters
    n = len(lowercase_s)
    for i in range(n // 2):
        if lowercase_s[i] != lowercase_s[n - i - 1]:
            return False
    return True


# Test the function
test_string = "Madam"
print(f"Is '{test_string}' a palindrome?:", isPalindrome(test_string))

test_string2 = "Hello"
print(f"Is '{test_string2}' a palindrome?:", isPalindrome(test_string2))


"""
python programme to remove all the duplicates from a given string
"""


def remove_duplicates(s):
    result = ""
    for ch in s:
        if ch not in result:  # Check if the character is not already in the result
            result += ch
    return result


# Example usage
string = "programming"
print("Original string:", string)
print("String without duplicates:", remove_duplicates(string))


"""
ask a sentence from a user then ask a integer K from a user print all the words which are equal or greater to K
"""


def filter_words_by_length():
    # Ask user for a sentence
    sentence = input("Enter a sentence: ")
    # Ask user for the integer K
    k = int(input("Enter an integer K: "))

    # Split the sentence into words
    words = sentence.split()

    # Filter words based on the length
    result = [word for word in words if len(word) >= k]

    print(f"Words with length equal or greater than {k}: {result}")


# Call the function
filter_words_by_length()


"""
Ask a string from a user replace all the Space(" ") with "-"
"""


def replace_spaces_with_ascii():
    # Ask user for a string
    user_input = input("Enter a string: ")

    # Replace spaces using ASCII values
    result = ""
    for char in user_input:
        if ord(char) == 32:  # ASCII value of space is 32
            result += "-"
        else:
            result += char

    print("String after replacing spaces with '-':", result)


# Call the function
replace_spaces_with_ascii()


"""
make a password stringht function and it will accept a string from a user and will return True 
or False depending on the strength of the password


a strong password has the following charecterstics

-Minumum eight charecters
-minimum One upper case alphabet
-minmum one lowe case alphabet
-contains at leat one Special symbol
-minimum one digit 
"""


def password_strength(password):
    # Check the length
    if len(password) < 8:
        return False

    # Initialize flags for each condition
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Loop through each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():  # Checks for special characters
            has_special = True

    # Check if all conditions are met
    return has_upper and has_lower and has_digit and has_special


# Test the function
password = input("Enter your password: ")
if password_strength(password):
    print("Password is strong.")
else:
    print("Password is weak.")


"""
keep asking charecter from the user until he presses q on the keyboard and change all the
upper case letter to lower case and vice versa
"""


def swap_case_input():
    while True:
        # Ask the user for input
        char = input("Enter a character (press 'q' to quit): ")

        # Check if the user pressed 'q' to quit
        if char == "q":
            break

        # Swap the case manually
        if char.isupper():
            swapped_char = char.lower()  # Convert to lowercase
        elif char.islower():
            swapped_char = char.upper()  # Convert to uppercase
        else:
            swapped_char = (
                char  # If it's neither (e.g., a special character), leave it unchanged
            )

        # Print the swapped character
        print("Swapped character:", swapped_char)


# Call the function
swap_case_input()
