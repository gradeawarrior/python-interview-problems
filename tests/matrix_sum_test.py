"""
Given an m x n matrix of rooms and each room having a random cost to enter the room:

          m
     --- --- ---
    | 1 | 3 | 2 |
     --- --- ---
  n | 1 | 5 | 7 |
     --- --- ---
    | 3 | 4 | 2 |
     --- --- ---

Generate a set of unique costs to travel from the top-left-most room to the bottom-right-most room.
Note that you can only travel in 2-directions: right or down from any given room.

The function will be passed in A as a list of lists:

Examples:

    A: [[0, 1], [1, 2]]
    r: set([3])

    A: [[1, 2, 3], [4, 5, 6]]
    r: set([12, 14, 16])
"""
import pytest
from project.matrix_sum import Solution


@pytest.mark.parametrize("test_input,expected", [
    ([[0, 1], [2, 3]], set([4, 5])),
    ([[0, 1], [1, 2]], set([3])),
    ([[1, 1, 3], [4, 5, 6]], set([11, 13, 16])),
    ([[1, 1, 3], [4, 5, 6], [7, 8, 9]], set([20, 22, 24, 25, 27, 29])),
    ])

def test_maze_sum_set(test_input, expected):
    assert Solution().maze_sum_set(test_input) == expected

