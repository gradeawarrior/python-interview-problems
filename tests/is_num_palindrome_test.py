"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

import pytest
from project.is_num_palindrome import Solution


@pytest.mark.parametrize("test_input, expected", [
    (-1, False),
    (0, True),
    (10, False),
    (11, True),
    (100, False),
    (123454321, True),
    (12345654321, True),
    (123456754321, False),
    ])

def test_is_palindrome(test_input, expected):
    assert Solution().isPalindrome(test_input) == expected
