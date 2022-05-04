import pytest
from group_anagrams import group_anagrams


@pytest.mark.parametrize(
    "strs, expected",
    (
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ),
)
def test_group_anagrams(strs, expected):
    assert expected == group_anagrams(strs)
