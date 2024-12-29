"""
Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""


def reverse(self, x: int) -> int:
    reversed_number = 0
    is_negative = False
    if x < 0:
        is_negative = True
        x = abs(x)

    while x > 0:
        last_digit = x % 10
        reversed_number = (reversed_number * 10) + last_digit
        x = x // 10

    if is_negative:
        reversed_number = reversed_number * -1

    if reversed_number < (-(2**31)) or reversed_number > (2**31 - 1):
        return 0

    return reversed_number
