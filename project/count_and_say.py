"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

    Input: 1
    Output: "1"

Example 2:

    Input: 4
    Output: "1211"
"""

def count_and_say():
    a = "1"
    while True:
        yield a

        # calculate next in sequence
        idx1, idx2 = 0, 1
        number = ""
        while idx1 < len(a):
            if idx2 < len(a) and a[idx2] == a[idx1]:
                idx2 += 1
            else:
                count = idx2 - idx1
                number += "%s%s" % (count, a[idx1])
                idx1 = idx2
                idx2 = idx1 + 1
        a = number

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        number = count_and_say()
        for i in xrange(0, n):
            result = number.next()
        return result
