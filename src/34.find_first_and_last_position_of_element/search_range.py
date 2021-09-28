"""
Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

Big O:
Time  -> O(Log(N))
Space -> O(1)
"""
from typing import List


class Solution:
    def get_left_position(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                if middle == 0 or nums[middle - 1] != target:
                    return middle
                right = middle - 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1

    def get_right_position(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left = 0
        right = size - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                if middle == size - 1 or nums[middle + 1] != target:
                    return middle
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1

    def search_range(self, nums: List[int], target: int) -> List[int]:
        left = self.get_left_position(nums, target)
        right = self.get_right_position(nums, target)
        return [left, right]
