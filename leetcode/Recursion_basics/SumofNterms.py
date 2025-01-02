"""
Sum of first n terms
Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

Examples:

Input: n = 5
Output: 225
Explanation: 13 + 23 + 33 + 43 + 53 = 225
Input: n = 7
Output: 784
Explanation: 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784
Constraints:
1 <= n <= 200 
"""


def sumOfSeries(n):
    if n == 0:
        return 0
    # Recursive call: Calculate the sum for (n - 1) and add n^3
    return n**3 + sumOfSeries(n - 1)


print(sumOfSeries(5))
