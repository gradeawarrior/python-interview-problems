"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0

Example 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
"""

import pytest
from project.median_two_sorted_arrays import Solution


@pytest.mark.parametrize("test_input1, test_input2, expected", [
    ([], [], 0.0),
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([2, 3, 4], [1], 2.5),
    ([1, 2, 3], [4], 2.5),
    ([2, 3], [1, 4], 2.5),
    ([2, 3], [1, 4, 5], 3.0),
    ([2, 3, 4], [1, 5], 3.0),
    ([2, 4], [1, 3, 5], 3.0),
    ([-3, -1], [-2], -2.0),
    ([-2, -1], [-4, -3], -2.5),

    ([1, 3, 5, 7, 9], [2, 4, 6, 8], 5.0),
    ([1, 2, 3, 4, 5], [6, 7, 8, 9], 5.0),
    ([1], [2, 3, 4, 5, 6, 7, 8, 9], 5.0),
    ([], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5.0),
    ([1, 2, 3, 4, 5, 6, 7, 8], [9], 5.0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [], 5.0),

    ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5.5),
    ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5),
    ([1], [2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
    ([], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [10], 5.5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], 5.5),

    ([11, 12, 13, 14, 15], [], 13.0),
    ([11, 12, 13, 14, 15, 16], [], 13.5),
    ([11, 13, 14, 15, 16], [12], 13.5),
    ])

def test_add_two_numbers(test_input1, test_input2, expected):
    actual = Solution().findMedianSortedArrays(test_input1, test_input2)
    assert actual == expected
    assert isinstance(actual, float)
