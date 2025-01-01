"""
LCM And GCD
Difficulty: BasicAccuracy: 37.02%Submissions: 182K+Points: 1
Given two integers a and b, write a function lcmAndGcd() to compute their LCM and GCD. The function inputs two integers a and b and returns a list containing their LCM and GCD.

Examples:

Input: a = 5 , b = 10
Output: [10, 5]
Explanation: LCM of 5 and 10 is 10, while their GCD is 5.
Input: a = 14 , b = 8
Output: [56, 2]
Explanation: LCM of 14 and 8 is 56, while their GCD is 2.
Input: a = 1 , b = 1
Output: [1, 1]
Explanation: LCM of 1 and 1 is 1, while their GCD is 1.
Expected Time Complexity: O(log(min(a, b))
Expected Auxiliary Space: O(1)

Constraints:
1 <= a, b <= 109
"""

from typing import List


def lcmAndGcd(self, a: int, b: int) -> List[int]:
    # Helper function to compute GCD using the Euclidean Algorithm
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    # Calculate GCD
    gcd_value = gcd(a, b)

    # Calculate LCM using the formula
    lcm_value = (a * b) // gcd_value

    # Return results as a list
    return [lcm_value, gcd_value]
