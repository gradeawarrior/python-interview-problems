"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

import project.config as config

numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

class Solution(object):
    def romanToInt(self, s):
        """
        Must handle subtraction for these cases

            IV = 4
            IX = 9
            XL = 40
            XC = 90
            CD = 400
            CM = 900

        :type s: str
        :rtype: int
        """
        if not s: return 0
        res = 0
        for ci in xrange(0, len(s)):
            pi = ci - 1 if (ci-1) >= 0 else None

            if config.debug:
                if pi is not None:
                    print("current: '%s' - ci: '%s' pi: '%s'" % (s[0:ci+1], s[ci], s[pi]))
                else:
                    print("current: '%s' - ci: '%s'" % (s[0:ci+1], s[ci]))

            if   pi is not None and s[ci] == "V" and s[pi] == "I": res += 3
            elif pi is not None and s[ci] == "X" and s[pi] == "I": res += 8
            elif pi is not None and s[ci] == "L" and s[pi] == "X": res += 30
            elif pi is not None and s[ci] == "C" and s[pi] == "X": res += 80
            elif pi is not None and s[ci] == "D" and s[pi] == "C": res += 300
            elif pi is not None and s[ci] == "M" and s[pi] == "C": res += 800
            else: res += numerals[s[ci]]
        return res
