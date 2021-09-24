import pytest
from boats_to_save_people import boats_to_save_people


@pytest.mark.parametrize(
    'people, limit, expected',
    [
        ([1, 2], 3, 1),
        ([3, 2, 2, 1], 3, 3),
        ([3, 5, 3, 4], 5, 4),
    ]
)
def test_move_zeros(people, limit, expected):
    assert expected == boats_to_save_people(people, limit)
