import pytest
from container_with_most_water import Solution


@pytest.mark.parametrize(
    'array, expected',
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([25], 0)
    ]
)
def test_move_zeros(array, expected):
    solution = Solution()
    assert expected == solution.max_area(array)
