"""
Given an array of integers arr, return true if and only if it is a valid
mountain array.

Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 104

Big O:
Time  -> O(N)
Space -> O(1)
"""
from typing import List


class Solution:
    def valid_mountain_array(self, array: List[int]) -> bool:
        size = len(array)

        if size < 3:
            return False

        left = 1

        while left < size and array[left] > array[left-1]:
            left += 1

        if (left == 1 or left == size):
            return False

        while left < size and array[left] < array[left-1]:
            left += 1

        return left == size
