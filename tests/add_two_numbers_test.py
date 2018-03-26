"""
You are given two non-empty linked lists representing two non-negative integers. The digits are
stored in reverse order and each of their nodes contain a single digit. Add the two numbers and
return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""

import pytest
from project.linkedlist import ListNode, convert_to_linkedlist, convert_to_number
from project.add_two_numbers import Solution


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

@pytest.mark.parametrize("test_input1, test_input2", [
    (1, 1),
    (9, 9),
    (12, 12),
    (123, 123),
    (1, 123),
    (123, 1),
    (12, 123),
    (123, 12),
    (10000, 10000000),
    ])

def test_add_two_numbers(test_input1, test_input2):
    ll1 = convert_to_linkedlist(test_input1)
    ll2 = convert_to_linkedlist(test_input2)
    actual = Solution().addTwoNumbers(ll1, ll2)
    assert convert_to_number(actual) == (test_input1 + test_input2)
