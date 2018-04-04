"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""

import project.config as config

# Overflow MIN_INT <= N < MAX_INT
MAX_INT = 2**31
MIN_INT = (2**31)*-1


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int

        A huge thanks for to the exceptional explaination here:

            https://leetcode.com/problems/divide-two-integers/discuss/13407/Detailed-Explained-8ms-C++-solution
        """
        # Exclude sign from the equation
        s = 1 if ((dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Do some pre-checks to optimize on division by 0 and 1, and anything
        # where dividend < divisor
        if divisor == 0: raise ValueError("Cannot divide by 0!")
        elif dividend == 0: return 0
        elif divisor > dividend: return 0

        r = 0
        while dividend >= divisor:
            # Shift bits until > dividend
            cd, multiplier = divisor, 1
            while dividend >= (cd << 1):
                cd <<= 1
                multiplier <<= 1
                if config.debug: print("Current number: %s - multiplier: %s" % (cd, multiplier))
            dividend -= cd
            r += multiplier

        # Add the sign back into before returning
        r = r if s > 0 else -r

        # Quickly check for overflow
        r = r - 1 if r >= MAX_INT else r
        r = r if r >= MIN_INT else MIN_INT

        if config.debug: print("Returning answer: %s" % r)
        return r

    def divide_bruteforce(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        s = 1 if ((dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend == 0: return 0
        elif divisor > dividend: return 0
        elif dividend == divisor: return 1*s
        elif divisor == 1 and dividend < MAX_INT and dividend >= MIN_INT: return dividend*s
        elif divisor == 1 and dividend >= MAX_INT and s > 0: return (MAX_INT-1)*s
        elif divisor == 1 and dividend >= MAX_INT and s < 0: return (MAX_INT)*s
        if divisor == 0: raise ValueError("Cannot divide by 0!")
        r = 0
        multiple = divisor
        while multiple <= dividend:
            r += 1
            multiple += divisor
            if multiple < divisor: r += 1
        return r * s

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            dividend = stringToInt(line)
            line = lines.next()
            divisor = stringToInt(line)

            ret = Solution().divide(dividend, divisor)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
