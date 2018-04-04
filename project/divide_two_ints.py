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
        """
        # Exclude sign from the equation
        s = 1 if ((dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Do some pre-checks to optimize on division by 0 and 1, and anything
        # where dividend < divisor
        if dividend == 0: return 0
        elif divisor > dividend: return 0
        elif dividend == divisor: return 1*s
        elif divisor == 1 and dividend < MAX_INT and dividend >= MIN_INT: return dividend*s
        elif divisor == 1 and dividend >= MAX_INT and s > 0: return (MAX_INT-1)*s
        elif divisor == 1 and dividend >= MAX_INT and s < 0: return (MAX_INT)*s
        if divisor == 0: raise ValueError("Cannot divide by 0!")

	# bitwise logic
        cd = divisor
        result = dividend
        shifter = 0
        # Keep shifting bits until 'dividend - shifted divisor' is negative
        while result > 0:
            cd = cd << 1
            shifter += 1
            result = dividend - cd
            if config.debug:
                print("Current number: %s - shifter: %s remainder=%s" % (cd, shifter, result))
        # Roll back 1 since the loop went over by 1,
        # except in situations where the difference is within divisor
        delta = result + divisor
        if result != 0 and (delta < 0 or delta >= divisor):
            shifter -= 1
            cd = cd >> 1

        # Calculate remainder and how many times divisor goes into dividend based on bit-logic
        remainder = dividend - cd
        if result == 0  or delta < 0 or delta >= divisor: r = 1 << shifter
        else: r = (1 << shifter) - 1
        if config.debug:
            print("Current answer: %s (shifter: %s) - remainder=%s" % (r, shifter, remainder))

        # Calculate if divisor will go into remainder anymore
        while  remainder > 0:
            remainder -= divisor
            if remainder >= 0: r += 1
            if config.debug: print("> updated answer: %s - remainder=%s" % (r, remainder))

        # Add the sign back into before returning
        if config.debug: print("Returning answer: %s" % r)
        return r*s

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
