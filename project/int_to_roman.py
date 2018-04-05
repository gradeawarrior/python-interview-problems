"""
Given an int, convert it to a roman numeral.

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
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num: return ""
        elif num < 0 or num >= 4000:
            raise ValueError("Roman Numerals not supported for negative ""numbers or numbers over 3999")
        res = ""

        while num > 0:
            if config.debug: print("number: %s - res: %s" % (num, res))
            if num >= 1000:
                temp = num/1000
                res += "".join(["M" for count in xrange(0, temp)])
                num %= 1000

            elif num >= 100 and num <= 999:
                temp = num/100
                if   num < 400: res += "".join(["C" for count in xrange(0, temp)])
                elif temp == 4: res += "CD"
                elif num >= 500 and num < 900: res += "D" + "".join(["C" for count in xrange(0, temp-5)])
                elif temp == 9: res += "CM"
                num %= 100

            elif num >= 10 and num < 100:
                temp = num/10
                if   num < 40: res += "".join(["X" for count in xrange(0, temp)])
                elif temp == 4: res += "XL"
                elif num >= 50 and num < 90: res += "L" + "".join(["X" for count in xrange(0, temp-5)])
                elif temp == 9: res += "XC"
                num %= 10

            elif num < 10:
                if   num < 4: res += ''.join(['I' for count in xrange(0, num)])
                elif num == 4: res += "IV"
                elif num == 5: res += "V"
                elif num > 5 and num < 9: res += "V" + ''.join(['I' for count in xrange(0, num-5)])
                elif num == 9: res += "IX"
                num /= 10

            else:
                raise AttributeError("I shouldn't have gotten here")

        return res
