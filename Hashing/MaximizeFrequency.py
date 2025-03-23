"""
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.



Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1
"""

from typing import List


def maxFrequency(self, nums: List[int], k: int) -> int:
    nums.sort()

    # Initialize pointers and variables
    left = 0
    current_cost = 0
    max_freq = 0

    # Iterate through the array with the right pointer
    for right in range(len(nums)):
        # Calculate the cost to make all elements in the window equal to nums[right]
        current_cost += (nums[right] - nums[right - 1]) * (right - left)

        # If the cost exceeds k, shrink the window from the left
        while current_cost > k:
            current_cost -= nums[right] - nums[left]
            left += 1

        # Update the max frequency
        max_freq = max(max_freq, right - left + 1)

    return max_freq
