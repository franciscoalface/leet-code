import pytest
from first_bad_version import Solution


@pytest.mark.parametrize(
    'n, bad, expected',
    [
        (5, 4, 4),
        (1, 1, 1),
        (38, 3, 3),
    ]
)
def test_move_zeros(n, bad, expected):
    solution = Solution(bad)
    assert expected == solution.first_bad_version(n)
