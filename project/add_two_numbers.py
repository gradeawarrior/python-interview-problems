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

from project.linkedlist import ListNode
import project.config as config

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
	dummy_node = ListNode(0)
        result = dummy_node
        carry = 0
        ptr1 = l1
        ptr2 = l2
        while ptr1 or ptr2:
            if config.debug and ptr1 and ptr2: print("%s + %s + %s" % (ptr1.val, ptr2.val, carry))
            elif config.debug and ptr1: print("%s (ptr1) + %s" % (ptr1.val, carry))
            elif config.debug and ptr2: print("%s (ptr2) + %s" % (ptr2.val, carry))
            t_sum = 0
            # add current numbers together
            if ptr1 and ptr2:
                t_sum = ptr1.val + ptr2.val + carry
            elif ptr1:
                t_sum = ptr1.val + carry
            elif ptr2:
                t_sum = ptr2.val + carry
            carry = 0

            # Update carry over if any
            if t_sum >= 10:
                node = ListNode(t_sum-10)
                carry = 1
            else:
                node = ListNode(t_sum)
            result.next = node
            result = result.next

            # Increase ptr1 and ptr2
            if ptr1: ptr1 = ptr1.next
            if ptr2: ptr2 = ptr2.next

        # Update carry over if any
        if carry > 0:
            node = ListNode(carry)
            result.next = node

	return dummy_node.next

