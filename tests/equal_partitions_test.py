"""
Given an array of integers and a partitions value, return True/False if the array can be
partitioned such that the sum of each partition equals the sum the each other.

Examples:

    A = [2, 3, 1, 4, 5]
    p = 3
    result: True because [[2, 3], [1, 4], [5]]

    A = [5, 2, 3, 1, 4]
    p = 3
    result: True because [[5], [2, 3], [1, 4]]

    A = [5, 5, 1, 2, 2]
    p = 3
    result: True because [[5], [5], [1, 2, 2]]

    A = [1, 2, 3, 4, 5]
    p = 3
    result: False
"""

import pytest
from project.equal_partitions import Solution


@pytest.mark.parametrize("A, partitions, expected", [
    ([2, 3, 1, 4, 5], 1, True),
    ([2, 3, 1, 4, 5], 3, True),
    ([5, 2, 3, 1, 4], 3, True),
    ([5, 5, 1, 2, 2], 3, True),
    ([5, 1, 2, 2, 5], 3, True),
    ([1, 2, 3, 4, 5], 3, False),
    ([2, 3, 1, 4, 5], 6, False),
    ([1, 1, -1, 1, 1], 3, True),
    ([1, 1, 1, 1, 1], 5, True),
    ([1, 1, 1, 1, 1, 1], 1, True),
    ([1, 1, 1, 1, 1, 1], 2, True),
    ([1, 1, 1, 1, 1, 1], 3, True),
    ([1, 1, 1, 1, 1, 1], 4, False),
    ([1, 1, 1, 1, 1, 1], 5, False),
    ([1, 1, 1, 1, 1, 1], 6, True),
    ])

def test_equal_partitions(A, partitions, expected):
    assert Solution().equalPartitions(A, partitions) == expected
