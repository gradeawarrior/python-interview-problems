
"""
Find the longest substring with at most with at most two distinct letters. Return the
length of that substring.
"""

import pytest
from project.longest_substring import Solution

"""
"eceba"
"ed"
"ece"
"fasting"
"banana"
"banana bananana"
"aac"
"ccaabbb"
"""
@pytest.mark.parametrize("test_input,expected", [
    (None, 0),
    ("a", 1),
    ("ed", 2),
    ("ece", 3),
    ("eceba", 3),
    ("fasting", 2),
    ("banana", 5),
    ("banana bananana", 7),
    ("aac", 3),
    ("ccaabbb", 5),
    ])

def test_longest_substring(test_input, expected):
    assert Solution().lengthOfLongestSubstringTwoDistinct(test_input) == expected

