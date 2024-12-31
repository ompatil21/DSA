"""
Problem: Sum of All Divisors from 1 to n
Given a positive integer n, calculate the value of ΣF(i) where i ranges from 1 to n, and F(i) is the sum of all divisors of i.
 
Examples:
# Input: n = 4
# Output: 15
# Explanation:
# F(1) = 1
# F(2) = 1 + 2 = 3
# F(3) = 1 + 3 = 4
# F(4) = 1 + 2 + 4 = 7
# Total = 1 + 3 + 4 + 7 = 15
 
# Input: n = 5
# Output: 21
# Explanation:
# F(1) = 1
# F(2) = 1 + 2 = 3
# F(3) = 1 + 3 = 4
# F(4) = 1 + 2 + 4 = 7
# F(5) = 1 + 5 = 6
# Total = 1 + 3 + 4 + 7 + 6 = 21
"""

"""
Approach 1:Better Method
    Explanation:
     - Loop through each number `i` from 1 to n.
     - For each `i`, find all its divisors `j` using another loop.
     - Add all these divisors to a running total.

# Time Complexity: O(n^2)
# Space Complexity: O(1)
"""


def sumOfDivisorsBetter(n):
    total_sum = 0
    for i in range(1, n + 1):  # Loop through each number from 1 to n
        for j in range(1, i + 1):  # Find divisors of i
            if i % j == 0:
                total_sum += j  # Add the divisor to the total sum
    return total_sum


"""
 Approach 2: Optimized Method
 Explanation:
     - Instead of finding divisors for each number, calculate how much each number contributes as a divisor.
     - A number `i` is a divisor of all its multiples. Its total contribution is `i * (n // i)`,
       where `n // i` is the count of numbers divisible by `i`.
 
 Time Complexity: O(n)
 Space Complexity: O(1)
"""


def sumOfDivisorsOptimized(n):
    total_sum = 0
    for i in range(1, n + 1):  # Each number `i` contributes to its multiples
        total_sum += i * (n // i)  # Add `i` multiplied by the count of multiples of `i`
    return total_sum


n = 5
print("Using Better Method:", sumOfDivisorsBetter(n))
print("Using Optimized Method:", sumOfDivisorsOptimized(n))
