# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def convert_to_linkedlist(number):
    """
    Converts a number (int) to a Linked List with the last digit as the first node.

    Examples:

        123 ==> [3, 2, 1]
        156 ==> [6, 5, 1]

    :param number: int - A number that needs converting to a Linked List
    :returns: ListNode - A Linked List representation of the specified number
    """
    if not isinstance(number, int): raise AttributeError("%s is not an int" % number)
    if number < 0: raise AttibuteError("%s is a negative number" % number)

    num_str = str(number)
    idx = len(num_str)-1
    dummy_root = ListNode(0)
    ptr = dummy_root
    while idx >= 0:
        node = ListNode(int(num_str[idx]))
        idx -= 1
        ptr.next = node
        ptr = ptr.next
    return dummy_root.next


def convert_to_number(ll):
    """
    Converts a Linked List back to a number

    Examples:

        [3, 2, 1] ==> 123
        [6, 5, 1] ==> 156

    :param ll: ListNode - A Linked List representation of a number
    :returns: int - a number
    """
    if not ll: return -1
    if not isinstance(ll, ListNode): raise AttributeError("ll should be a ListNode or None")

    ptr = ll
    result = ""
    while(ptr):
        result = str(ptr.val) + result
        ptr = ptr.next
    return int(result) if result else -1
