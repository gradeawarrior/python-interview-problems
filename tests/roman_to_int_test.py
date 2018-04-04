"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

import pytest
from project.roman_to_int import Solution


@pytest.mark.parametrize("test_input, expected", [
    (None, 0),
    ("", 0),
    ("I", 1),
    ("II", 2),
    ("III", 3),
    ("IV", 4),
    ("V", 5),
    ("VI", 6),
    ("VII", 7),
    ("VIII", 8),
    ("IX", 9),
    ("X", 10),
    ("XIV", 14),
    ("XIX", 19),
    ("XLIX", 49),
    ("XL", 40),
    ("L", 50),
    ("XC", 90),
    ("C", 100),
    ("CD", 400),
    ("D", 500),
    ("CM", 900),
    ("M", 1000),
    ("MCD", 1400),
    ("MD", 1500),
    ])

def test_is_palindrome(test_input, expected):
    assert Solution().romanToInt(test_input) == expected
