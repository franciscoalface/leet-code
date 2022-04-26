import pytest
from best_time_to_buy_and_sell_stock import max_profit2


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2, 4], 3),
        ([3, 2, 6, 5, 0, 3], 4),
        ([2, 1, 2, 1, 0, 1, 2], 2),
    ],
)
def test_two_sum(prices, expected):
    assert expected == max_profit2(prices)
