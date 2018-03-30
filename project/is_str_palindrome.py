"""
Determine whether an String is a palindrome. Do this without extra space.
"""

import project.config as config

class Solution(object):
    def isPalindrome(self, s):
        """
        :type x: int
        :rtype: bool
        """
        if not s: return False
        if len(s) == 1: return True
        idx1 = 0
        idx2 = len(s) - 1
        while idx1 < idx2:
            if s[idx1] != s[idx2]: return False
            idx1 += 1
            idx2 -= 1
        return True

