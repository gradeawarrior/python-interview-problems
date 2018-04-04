"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""

import pytest
from project.divide_two_ints import Solution


@pytest.mark.parametrize("dividend, divisor, expected", [
    (1, 2, 0),
    (2, 2, 1),
    (3, 2, 1),
    (4, 2, 2),
    (5, 2, 2),
    (6, 2, 3),
    (8, 2, 4),
    (15, 3, 5),
    (1, -1, -1),
    (-1, -1, 1),
    (2147483648, 1, 2147483647),
    (-2147483648, -1, 2147483647),
    (2147483648, -1, -2147483648),
    (-2147483648, 1, -2147483648),
    (2147483647, 2, 1073741823),
    (2147483647, 3, 715827882),
    (2147483647, 4, 536870911),
    (2147483647, 5, 429496729),
    (2147483647, 6, 357913941),
    (2147483647, 7, 306783378),
    (2147483647, 8, 268435455),
    (2147483647, 9, 238609294),
    (2147483647, 10, 214748364),
    (2147483647, 11, 195225786),
    (2147483647, 12, 178956970),
    (2147483647, 13, 165191049),
    (2147483647, 14, 153391689),
    (2147483647, 15, 143165576),
    (2147483647, 16, 134217727),
    ])

def test_division(dividend, divisor, expected):
    assert Solution().divide(dividend, divisor) == expected

@pytest.mark.parametrize("dividend, divisor, expected", [
    (1, 2, 0),
    (2, 2, 1),
    (3, 2, 1),
    (4, 2, 2),
    (5, 2, 2),
    (6, 2, 3),
    (8, 2, 4),
    (15, 3, 5),
    (1, -1, -1),
    (-1, -1, 1),
    (2147483648, 1, 2147483647),
    (-2147483648, -1, 2147483647),
    (2147483648, -1, -2147483648),
    (-2147483648, 1, -2147483648),
    ])

def test_division_bruteforce(dividend, divisor, expected):
    """
    NOTE: This is an unoptimized implementation, so it is not doing 2147483647 / 2
    """
    assert Solution().divide_bruteforce(dividend, divisor) == expected
