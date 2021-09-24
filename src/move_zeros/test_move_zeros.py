import pytest
from move_zeros import move_zeros


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([2, 0, 11, 0, 15], [2, 11, 15, 0, 0]),
        ([0, 1, 2, 3, 4], [1, 2, 3, 4, 0]),
        ([3, 3, 0, 1, 9, 0, 12, 0], [3, 3, 1, 9, 12, 0, 0, 0]),
    ]
)
def test_move_zeros(nums, expected):
    assert expected == move_zeros(nums)
