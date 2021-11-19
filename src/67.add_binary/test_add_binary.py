import pytest
from add_binary import Solution


@pytest.mark.parametrize(
    'a, b, expected',
    [
        ('11', '1', '100'),
        ('1010', '1011', '10101'),
    ]
)
def test_add_binary(a: str, b: str, expected: str):
    solution = Solution()
    assert expected == solution.add_binary(a, b)
