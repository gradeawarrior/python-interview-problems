"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum
length of s is 1000.

Example:

    Input: "babad"
    Output: "bab"

    Note: "aba" is also a valid answer.

Example:

    Input: "cbbd"
    Output: "bb"
"""

import pytest
from project.longest_palindrome_substr import Solution


@pytest.mark.parametrize("test_input, expected", [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("", ""),
    ("a", "a"),
    ("ab", "a"),
    ("abc", "a"),
    ("abcdd", "dd"),
    ("abcdefghijklmnopqrstuvwxyz", "a"),
    ("abcdefghijklmmnopqrstuvwxyz", "mm"),
    ("abcdefghijklmnopqrstuvwxyzz", "zz"),
    ("abcdefghijklmnopqrstuvwxyzzz", "zzz"),
    ])

def test_add_two_numbers(test_input, expected):
    assert Solution().longestPalindrome(test_input) == expected
