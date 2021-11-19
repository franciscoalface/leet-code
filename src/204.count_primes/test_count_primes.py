import pytest
from count_primes import Solution


@pytest.mark.parametrize(
    'num, expected',
    [
        (10, 4),
        (0, 0),
        (1, 0),
    ]
)
def test_count_primes(num, expected):
    solution = Solution()
    assert expected == solution.count_primes(num)
