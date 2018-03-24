import pytest
from project.min_window_substring import Solution

@pytest.mark.parametrize("test_string, test_chars, expected", [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("abc", "bc", "bc"),
    ("ab", "b", "b"),
    ("bba", "ba", "ba"),
    ("aaflslflsldkalskaaa", "aaa", "aaa"),
    ("acbbaca", "aba", "baca"),
    ])

def test_min_window_substring(test_string, test_chars, expected):
    result = Solution().minWindow(test_string, test_chars)
    assert result == expected
