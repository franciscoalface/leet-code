import pytest
from robot_return_to_origin import Solution


@pytest.mark.parametrize(
    'moves, expected',
    [
        ('UDRL', True),
        ('UD', True),
        ('LL', False),
        ('RRDD', False),
        ('LDRRLRUULR', False),
    ]
)
def test_robot_return_to_origin(moves: str, expected: bool):
    solution = Solution()
    assert expected == solution.robot_return_to_origin(moves)
