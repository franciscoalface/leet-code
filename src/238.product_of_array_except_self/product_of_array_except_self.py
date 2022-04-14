import pytest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]
        right_prod = [1]
        result = []

        for num in nums[:-1]:
            left_prod.append(num * left_prod[-1])

        for num in reversed(nums[1:]):
            right_prod.append(num * right_prod[-1])

        right_prod = right_prod[::-1]

        for index, _ in enumerate(nums):
            result.append(left_prod[index] * right_prod[index])

        return result

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        size = len(nums)

        left = 1
        for index in range(size):
            result[index] = left
            left *= nums[index]

        right = 1
        for index in range(size - 1, -1, -1):
            result[index] *= right
            right *= nums[index]

        return result


@pytest.mark.parametrize(
    "args, result",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ],
)
def test_product_of_array_except_self(args, result):
    solution = Solution()
    assert solution.productExceptSelf2(args) == result


# solution = Solution()
# solution.productExceptSelf2([1, 2, 3, 4])
