"""
Write a function:

def solution(A)
that, given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.
Given A = [-1, -3], the function should return 1.

Assume that:
- N is an integer within the range [1..100,000];
- each element of array A is an integer within the range [-1,000,000..1,000,000].

Complexity:
- expected worst-case time complexity is O(N);
- expected worst-case space complexity is O(N), beyond input storage
  (not counting the storage required for input arguments).
"""

import pytest
from time import time
from project.smallest_possible_integer import solution1, solution2, solution3
import project.config as config


@pytest.mark.parametrize("test_input,expected", [
    ([1,3,6,4,1,2], 5),
    ([1,2,3], 4),
    ([-1, -3], 1),
    ([1, 2, 3], 4),
    ([-1,-2,-3,-4,80,82], 1),
    ([80], 1),
    ([1,2,3,80], 4),
    ])

def test_smallest_possible_integer_solution1(test_input, expected):
    """
    Assumes A is an unsorted list and this implementation makes no attempt at pre-sorting numbers.
    """
    start = time()
    assert solution1(test_input) == expected
    duration = (time() - start) * 1000
    if config.debug: print("duration = %.2f ms" % duration)
    assert duration < 10, "Expecting operation to take < 10 ms"

@pytest.mark.parametrize("test_input,expected", [
    ([1,3,6,4,1,2], 5),
    ([1,2,3], 4),
    ([-1, -3], 1),
    ([1, 2, 3], 4),
    ([-1,-2,-3,-4,80,82], 1),
    ([80], 1),
    ([1,2,3,80], 4),
    ])

def test_smallest_possible_integer_solution2(test_input, expected):
    """
    Assumes A is an unsorted list and this implementation pre-sorts the numbers.
    """
    start = time()
    assert solution2(test_input) == expected
    duration = (time() - start) * 1000
    if config.debug: print("duration = %.2f ms" % duration)
    assert duration < 10, "Expecting operation to take < 10 ms"

@pytest.mark.parametrize("test_input,expected", [
    ([1,3,6,4,1,2], 5),
    ([1,2,3], 4),
    ([-1, -3], 1),
    ([1, 2, 3], 4),
    ([-1,-2,-3,-4,80,82], 1),
    ([80], 1),
    ([1,2,3,80], 4),
    ])

def test_smallest_possible_integer_solution3(test_input, expected):
    """
    Assumes A is an unsorted list and this implementation pre-sorts the numbers. It also attempts
    """
    start = time()
    assert solution3(test_input) == expected
    duration = (time() - start) * 1000
    if config.debug: print("duration = %.2f ms" % duration)
    assert duration < 10, "Expecting operation to take < 10 ms"

