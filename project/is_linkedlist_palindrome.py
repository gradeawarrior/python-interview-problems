"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
----------

Could you do it in O(n) time and O(1) space?
"""

from project.linkedlist import ListNode
import project.config as config

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        elif not head.next: return True
        ptr1 = head
        ptr2 = ptr1
        half = [ptr1.val]
        l = 1

        while ptr1.next:
            if config.debug: print("ptr2.next (%s) and ptr2.next.next (%s)" %
                    (ptr2.next is not None, (ptr2.next is not None and ptr2.next.next is not None)))
            while ptr2.next and ptr2.next.next:
                ptr1 = ptr1.next
                half.append(ptr1.val)
                if ptr2.next: l += 1
                if ptr2.next.next: l += 1
                ptr2 = ptr2.next.next
            if ptr2.next:
                l += 1
                ptr2 = ptr2.next
            calculated_half = (l/2)
            if l % 2 == 1 and len(half) > calculated_half: half.pop()
            if config.debug: print("half: %s - l=%s - calculated_half=%s" % (half, l, calculated_half))

            ptr1 = ptr1.next
            top = half.pop() if half else None

            # Some precondition checks
            if config.debug: print("current: %s top: %s - ptr1.next: %s len(half): %s" %
                    (ptr1.val, top, (ptr1.next is not None), len(half)))
            if top is None: return False
            if ptr1.next and len(half) == 0: return False

            if config.debug: print("  > Checking '%s' == '%s' ?" % (top, ptr1.val))
            if top != ptr1.val: return False
        if config.debug: print("> Returning True")
        return True
