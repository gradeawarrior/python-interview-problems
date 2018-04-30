"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

    Input: 1
    Output: "1"

Example 2:

    Input: 4
    Output: "1211"
"""

import pytest
from project.count_and_say import Solution


@pytest.mark.parametrize("test_input, expected", [
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (4, "1211"),
    (5, "111221"),
    (6, "312211"),
    (7, "13112221"),
    (8, "1113213211"),
    (9, "31131211131221"),
    (10, "13211311123113112211"),
    ])

def test_count_and_say(test_input, expected):
    assert Solution().countAndSay(test_input) == expected
