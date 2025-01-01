"""
9. Palindrome Number

Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1

"""


def isPalindrome(self, x: int) -> bool:
    # Check for cases where the number cannot be a palindrome:
    # - Negative numbers are not palindromes.
    # - Numbers ending in 0 (except 0 itself) are not palindromes.
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    # Special case: 0 is a palindrome.
    if x == 0:
        return True

    # Initialize a variable to store the reversed half of the number.
    reversed_half = 0

    # Store the original number for comparison (not strictly necessary here).
    original_x = x

    # Reverse the second half of the number while comparing it with the first half.
    while x > reversed_half:
        # Add the last digit of x to reversed_half.
        reversed_half = reversed_half * 10 + x % 10
        # Remove the last digit from x.
        x //= 10

    # Check if the first half (x) matches the reversed second half (reversed_half).
    # For odd-length numbers, ignore the middle digit by dividing reversed_half by 10.
    return x == reversed_half or x == reversed_half // 10
