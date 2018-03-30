"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

import project.config as config

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        if x >= 0 and x < 10: return True
        if x % 10 == 0: return False
        r = 0
        while x > r:
            r = (r * 10) + (x % 10)
            x /= 10
        if config.debug: print("%s == %s (%s)" % (x, r, r/10))
        return (x == r or x == (r/10))

