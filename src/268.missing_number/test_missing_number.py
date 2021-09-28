import pytest
from missing_number import Solution1, Solution2


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
        ([1], 0)
    ]
)
def test_move_zeros_solution1(nums, expected):
    solution = Solution1()
    assert expected == solution.missing_number(nums)


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
        ([1], 0)
    ]
)
def test_move_zeros_solution2(nums, expected):
    solution = Solution2()
    assert expected == solution.missing_number(nums)
