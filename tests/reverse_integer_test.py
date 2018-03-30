"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

    Input: 123
    Output:  321

Example 2:

    Input: -123
    Output: -321

Example 3:

    Input: 120
    Output: 21

Note:
====

Assume we are dealing with an environment which could only hold integers within the 32-bit signed
integer range. For the purpose of this problem, assume that your function returns 0 when the
reversed integer overflows.
"""

import pytest
from project.reverse_integer import Solution


# 2,147,483,647
@pytest.mark.parametrize("test_input, expected", [
    (-1234567893, 0),
    (-123, -321),
    (-12, -21),
    (-1, -1),
    (1, 1),
    (12, 21),
    (123, 321),
    (1234567893, 0),
    ])

def test_add_two_numbers(test_input, expected):
    assert Solution().reverse(test_input) == expected
