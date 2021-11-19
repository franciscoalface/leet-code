import pytest
from single_number import Solution
from typing import List


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ]
)
def test_single_number(nums: List[int], expected: int):
    solution = Solution()
    assert expected == solution.single_number(nums)
