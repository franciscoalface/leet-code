import pytest
from search_range import Solution


@pytest.mark.parametrize(
    'nums, target, expected',
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
    ]
)
def test_move_zeros(nums, target, expected):
    solution = Solution()
    assert expected == solution.search_range(nums, target)
