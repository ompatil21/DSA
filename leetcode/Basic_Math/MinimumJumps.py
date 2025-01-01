"""
Minimum Jumps
Difficulty: MediumAccuracy: 11.91%Submissions: 924K+Points: 4
Given an array arr[] of non-negative integers. Each array element represents the maximum length of the jumps that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x. Find the minimum number of jumps to reach the end of the array starting from the first element. If an element is 0, then you cannot move through that element.

Note:  Return -1 if you can't reach the end of the array.

Examples : 

Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
Output: 3 
Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 
Input: arr = [1, 4, 3, 2, 6, 7]
Output: 2 
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.
Input: arr = [0, 10, 20]
Output: -1
Explanation: We cannot go anywhere from the 1st element.
Constraints:
2 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 105

"""


def minJumps(self, arr):
    n = len(arr)
    if n == 1:
        return 0  # Already at the last index
    if arr[0] == 0:
        return -1  # Cannot move anywhere

    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(n):
        # Update the farthest position reachable
        farthest = max(farthest, i + arr[i])

        # If we have reached the end of the current range
        if i == current_end:
            jumps += 1
            current_end = farthest

            # Check if we have reached the end
            if current_end >= n - 1:
                return jumps

        # If stuck, return -1
        if i >= farthest:
            return -1

    return -1
