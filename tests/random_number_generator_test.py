"""
There is a company that has a vry creative way of managing its accounts. Every time they want to
write down a number, they shuffle its digits in the following way; they alternatively write one
digit from the front of the number and one digit from the back, then the second digit from the
front and the second from the back, and so on until the length of the shuffled number is the same
as that of the original.

Write a function

    def randomize(A)

that, given a positive integer A, returns its shuffled representation.

For example:

    Given A = 123456 the function should return 162534.
    Given A = 130 the function should return 103.

Assume that:

- A is an integer within the range [0..100,000,000].

In your solution, focus on correctness. The performance of your solution will not be the focus of
the assessment.
"""

import pytest
from project.random_number_generator import Solution


@pytest.mark.parametrize("test_input,expected", [
    (0, 0),
    (1, 1),
    (35, 35),
    (130, 103),
    (123, 132),
    (1234, 1243),
    (12345, 15423),
    (123456, 162534),
    (1234567, 1726534),
    (12345678, 18237645),
    (123456789, 192873645),
    (1234567890, 1029384756),
])

def test_random_number_solution1(test_input, expected):
    assert Solution().randomize_solution1(test_input) == expected
    # assert Solution().randomize_solution2(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    (0, 0),
    (1, 1),
    (35, 35),
    (130, 103),
    (123, 132),
    (1234, 1423), # different
    (12345, 15243), # different
    (123456, 162534),
    (1234567, 1726354), # different
    (12345678, 18273645), # different
    (123456789, 192837465), # different
    (1234567890, 1203948576), # different
])

def test_random_number_solution2(test_input, expected):
    assert Solution().randomize_solution2(test_input) == expected

@pytest.mark.parametrize("test_input", [
    (1234), # different
    (12345), # different
    (1234567), # different
    (12345678), # different
    (123456789), # different
    (1234567890), # different
])

def test_random_number_solution1_and_solution2_different(test_input):
    """
    Proving that this question is flawed and that two answers that produce deterministic
    results, can still have alternative answers for other numbers in the range [0..100,000,000]
    """
    sol1 = Solution().randomize_solution1(test_input)
    sol2 = Solution().randomize_solution2(test_input)
    assert sol1 != sol2, "Two algorithms can answer the question, but still get different results"

@pytest.mark.parametrize("test_input", [
    (0),
    (1),
    (35),
    (130), # example given in question
    (123),
    (123456), # example given in question
])

def test_random_number_solution1_and_solution2_similarities(test_input):
    """
    Proving that this question is flawed and that two answers that produce deterministic
    results, can still have alternative answers for other numbers in the range [0..100,000,000]
    """
    sol1 = Solution().randomize_solution1(test_input)
    sol2 = Solution().randomize_solution2(test_input)
    assert sol1 == sol2, "Two algorithms can answer the question, but still get different results"
