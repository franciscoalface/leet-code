import pytest
from valid_mountain import Solution


@pytest.mark.parametrize(
    'array, expected',
    [
        ([2, 1], False),
        ([3, 5, 5], False),
        ([0, 3, 2, 1], True),
        ([0, 2, 3, 4, 5, 2, 1], True)
    ]
)
def test_move_zeros(array, expected):
    solution = Solution()
    assert expected == solution.valid_mountain_array(array)
