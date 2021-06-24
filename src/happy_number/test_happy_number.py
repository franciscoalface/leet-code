import pytest
from happy_number import happy_number


@pytest.mark.parametrize(
    'n, expected',
    [
        (19, True),
        (2, False),
    ]
)
def test_reverse_string(n, expected):
    assert expected == happy_number(n)
