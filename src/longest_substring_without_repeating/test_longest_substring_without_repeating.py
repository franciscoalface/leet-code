import pytest
from longest_substring_without_repeating import Solution


@pytest.mark.parametrize(
    's, expected',
    [
        ('abcabcbb', 3),
        ('bbbbb', 1),
        ('pwwkew', 3),
        ('', 0)
    ]
)
def test_move_zeros(s, expected):
    solution = Solution()
    assert expected == solution.length_of_longest_substring(s)
