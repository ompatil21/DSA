"""
Reverse an Array
You are given an array of integers arr[]. Your task is to reverse the given array.

Examples:

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element
goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.

Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.

Input: arr = [1]
Output: [1]
Explanation: The array has only single element, hence the reversed array is same as the original.

Constraints:
1<=arr.size()<=105
0<=arr[i]<=105
"""


# without recursion best approach
def reverse_arry(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


arr1 = [1, 2, 3, 4, 5]
print(reverse_arry(arr1))


# with recursion


def revAr(arr, ind):
    n = len(arr)
    # Base case: Stop when the middle of the array is reached
    if ind >= n // 2:
        print(arr)  # Print the reversed array
        return
    # Swap elements at index `ind` and `n-1-ind`
    arr[ind], arr[n - 1 - ind] = arr[n - 1 - ind], arr[ind]
    # Recursive call for the next index
    revAr(arr, ind + 1)


arr = [1, 2]
revAr(arr, 0)
