"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""

import pytest
from project.longest_common_prefix import Solution


@pytest.mark.parametrize("test_input, expected", [
    ([], ""),
    (["flower"], "flower"),
    (["flower", "flow", "flight"], "fl"),
    (["flower", "flowery", "flowflower"], "flow"),
    (["hello", "world"], ""),
    (["hello", "hi", "world"], ""),
    (["dog","racecar","car"], ""),
    (["aca","cba"], ""),
    ])

def test_longest_common_prefix(test_input, expected):
    assert Solution().longestCommonPrefix(test_input) == expected
