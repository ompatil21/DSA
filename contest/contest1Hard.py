"""
make function named reverse which accepts an integer n reverse the number passed 
as a parameter and return the reverse number Do not use strings
"""


def reverse(n):
    reverse_number = 0
    is_negative = False
    if n < 0:
        is_negative = True
        n = n * (-1)

    while n > 0:
        last_digit = n % 10
        reverse_number = (reverse_number * 10) + last_digit
        n = n // 10

    if is_negative:
        reverse_number = reverse_number * (-1)

    return reverse_number


print(reverse(35))


"""
make a fucntion check palindrome which accepts an integer n from user and return true if its palindrom 
or else returns false
"""


def checkPalindrome(n):
    reverse_number = 0
    original_n = n
    if n < 0:
        return False

    while n > 0:
        last_digit = n % 10
        reverse_number = (reverse_number * 10) + last_digit
        n = n // 10

    if reverse_number == original_n:
        return True
    return False


print(checkPalindrome(335))


"""
make a function Printwords which accepts an integer n from the user ans print number as words
"""


def printWords(n):
    if n == 0:
        return "Zero"

    result = []
    while n > 0:
        last_digit = n % 10
        if last_digit == 1:
            result.append("One")
        elif last_digit == 2:
            result.append("Two")
        elif last_digit == 3:
            result.append("Three")
        elif last_digit == 4:
            result.append("Four")
        elif last_digit == 5:
            result.append("Five")
        elif last_digit == 6:
            result.append("Six")
        elif last_digit == 7:
            result.append("Seven")
        elif last_digit == 8:
            result.append("Eight")
        elif last_digit == 9:
            result.append("Nine")
        elif last_digit == 0:
            result.append("Zero")

        n //= 10  # Remove the last digit

    # Since we processed digits from last to first, reverse the result list
    result.reverse()
    return " ".join(result)


print(printWords(81))


"""
make a function named checkArmstrong and returs True if the number is Armstrong number or else returns False
"""


def check_armstrong(n):
    original_n = n
    no_of_digits = 0
    temp = n

    # Count the number of digits in the number
    while temp > 0:
        no_of_digits += 1
        temp //= 10

    new_number = 0
    temp = n

    # Calculate the sum of each digit raised to the power of no_of_digits
    while temp > 0:
        last_digit = temp % 10
        new_number += last_digit**no_of_digits
        temp //= 10

    # Check if the sum matches the original number
    return new_number == original_n


print(check_armstrong(153))
print(check_armstrong(53))
print(check_armstrong(9474))


"""
make a funtion named firstandLast in which it gives sum of first and last digit of a number 
"""


def sumfirstandlast(n):
    last_digit = n % 10  # The last digit is n % 10

    # To find the first digit, keep dividing the number by 10 until it becomes less than 10
    while n >= 10:
        n = n // 10
    first_digit = n  # After division, n becomes the first digit

    sum_of_digits = first_digit + last_digit
    return sum_of_digits


print(sumfirstandlast(145))
