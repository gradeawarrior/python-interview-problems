"""
Given an integer, convert to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

import pytest
from project.int_to_roman import Solution


@pytest.mark.parametrize("expected, test_input", [
    ("", None),
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
    ("CDI", 401),
    ("D", 500),
    ("DI", 501),
    ("CM", 900),
    ("CMI", 901),
    ("M", 1000),
    ("MCD", 1400),
    ("MD", 1500),
    ("MM", 2000),
    ("MMM", 3000),
    ("MMMCMXCIX", 3999),
    ])

def test_int_to_roman_numeral(test_input, expected):
    assert Solution().intToRoman(test_input) == expected
