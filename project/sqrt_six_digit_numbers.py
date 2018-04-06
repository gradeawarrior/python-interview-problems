"""
Find all 6-digit numbers where the sum of the first 3-digits of the number plus the
last 3-digits of the number equals the square-root of the original 6-digit number.
"""

import math
import project.config as config


class Solution():
    def find_six_digit_number(self):
        """
        :returns: List - a List of six digit numbers
        """
        ret = []
        for number in xrange(100000, 1000000):
            str_number = str(number)
            part1 = int(str_number[0:3])
            part2 = int(str_number[3:6])
            if (part1 + part2) == math.sqrt(number):
                if config.debug: print("%s + %s == math.sqrt(%s)" % (part1, part2, number))
                ret.append(number)
        return ret


def main():
    numbers = Solution().find_six_digit_number()
    print("numbers: %s" % numbers)

if __name__ == "__main__":
    main()
