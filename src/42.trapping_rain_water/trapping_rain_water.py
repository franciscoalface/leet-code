"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
"""
from typing import List
import pytest


def trap(height: List[int]) -> int:
    total_water = 0
    left = 0
    right = len(height) - 1
    max_left = 0
    max_right = 0

    while left < right:
        if height[right] > height[left]:
            if max_left > height[left]:
                total_water += max_left - height[left]
            else:
                max_left = height[left]
            left += 1
        else:
            if max_right > height[right]:
                total_water += max_right - height[right]
            else:
                max_right = height[right]
            right -= 1

    return total_water


@pytest.mark.parametrize("args, result", [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2], 8)
])
def test_product_of_array_except_self(args, result):
    assert trap(args) == result
