"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

import pytest
from project.linkedlist import ListNode
from project.is_linkedlist_palindrome import Solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def convert_str_to_ll(s):
    if not s: return None
    dummy_node = ListNode(0)
    result = dummy_node
    for char in s:
        # Attempt to convert to an int
        try:
            char = int(char)
        except:
            pass
        result.next = ListNode(char)
        result = result.next
    return dummy_node.next

@pytest.mark.parametrize("test_input, expected", [
    (None, True),
    ("", True),
    ("a", True),
    ("aa", True),
    ("ab", False),
    ("1", True),
    ("2", True),
    ("3", True),
    ("10", False),
    ("11", True),
    ("100", False),
    ("101", True),
    ("1001", True),
    ("123454321", True),
    ("12345654321", True),
    ("123456754321", False),
    ("1213", False),
    ("13441", False),
    ])

def test_is_palindrome(test_input, expected):
    ll = convert_str_to_ll(test_input)
    assert Solution().isPalindrome(ll) == expected
