import pytest
from find_first_and_last_position_of_element import Solution2


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
    ],
)
def test_find_first_and_last_position_of_element(nums, target, expected):
    solution = Solution2()
    assert expected == solution.search_range(nums, target)
