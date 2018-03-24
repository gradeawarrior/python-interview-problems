import pytest
from project.move_zeroes import Solution

"""
[0,1,0,3,12]
[1,0,0,3,12]
[0,1,0]
[0,0,1]
[0,1,1]
"""
@pytest.mark.parametrize("test_input,expected", [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([1,0,0,3,12], [1,3,12,0,0]),
    ([0,1,0], [1,0,0]),
    ([0,1,1], [1,1,0])
    ])

def test_move_zeroes(test_input, expected):
    # Note: This is modifying the list in place. Nothing is returned from this function
    result = Solution().moveZeroes(test_input)
    assert result is None
    assert test_input == expected
