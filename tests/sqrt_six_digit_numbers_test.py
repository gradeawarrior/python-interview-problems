"""
Find all 6-digit numbers where the sum of the first 3-digits of the number plus the
last 3-digits of the number equals the square-root of the original 6-digit number.
"""

import pytest
from project.sqrt_six_digit_numbers import Solution


@pytest.skip
def test_sqrt_numbers():
    assert Solution().find_six_digit_number() == [494209, 998001]
