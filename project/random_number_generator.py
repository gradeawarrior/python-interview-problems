"""
There is a company that has a vry creative way of managing its accounts. Every time they want to
write down a number, they shuffle its digits in the following way; they alternatively write one
digit from the front of the number and one digit from the back, then the second digit from the
front and the second from the back, and so on until the length of the shuffled number is the same
as that of the original.

Write a function

    def randomize(A)

that, given a positive integer A, returns its shuffled representation.

For example, given A = 123456 the function should return 162534.

Given A = 130 the function should return 103.

Assume that:

- A is an integer within the range [0..100,000,000].

In your solution, focus on correctness. The performance of your solution will not be the focus of
the assessment.
"""

import math
import project.config as config


class Solution():
    def randomize_solution1(self, A):
        # Optimize on 3 digit numbers and higher
        if A < 100: return A

        # Convert to something I can enumerate over digits
        str_array = [digit for digit in str(A)]
        number_of_iterations = int(math.ceil(len(str_array)/2.0))
        random_number = [None for digit in str_array]
        idx1 = 0
        idx2 = len(str_array)-1

        for i in range(0, number_of_iterations):
            remaining_digits = [digit for digit in str_array if digit is not None]
            remaining_indices = [idx for idx,digit in enumerate(str_array) if digit is not None]
            mid_idx_orig = len(remaining_indices)//2
            mid_idx_orig_minus = len(remaining_indices)//2 - 1
            mid_idx = len(remaining_digits)//2
            mid_idx_minus = len(remaining_digits)//2 - 1
            if config.debug: print("remaining: %s - mid: %s - random: %s - orig: %s" %
                  (remaining_digits, mid_idx, random_number, str_array))

            # For the final inner number(s) when there is only 1 or 2 digits left
            if len(remaining_digits) <= 2:
                for digit in remaining_digits:
                    random_number[idx1] = digit
                    idx1 += 1
                break

            # keep outermost front; and move mid-number to back
            if i % 2 == 0:
                random_number[idx1] = remaining_digits[0]
                random_number[idx2] = remaining_digits[mid_idx]
                # Reset indices and original str_array
                str_array[remaining_indices[0]] = None
                str_array[remaining_indices[mid_idx_orig]] = None
                idx1 += 1
                idx2 -= 1

            # move back number to front; and move mid-number to back
            else:
                random_number[idx1] = remaining_digits[-1]
                random_number[idx2] = remaining_digits[mid_idx_minus]
                # Reset indices and original str_array
                str_array[remaining_indices[-1]] = None
                str_array[remaining_indices[mid_idx_orig_minus]] = None
                idx1 += 1
                idx2 -= 1

        return int("".join(random_number))

    def randomize_solution2(self, A):
        if A / 10 == 0:
            return A

        original_A = A

        # find length of account number
        max_divisor = 100000000
        divisor = max_divisor
        while (original_A / divisor) == 0:
            original_A %= divisor # strip off leading zeros
            divisor /= 10

        new_A = 0
        while divisor > 0:
            left = original_A / divisor
            right = original_A % 10
            if config.debug: print("original left = %s, right = %s" % (left, right))

            work_new_A = left * divisor
            original_A -= work_new_A

            divisor /= 10
            right *= divisor

            work_new_A += right
            original_A /= 10
            new_A += work_new_A
            if config.debug: print("original = %s" % original_A)
            if config.debug: print("work new = %s" % work_new_A)
            if config.debug: print("new = %s" % new_A)

            divisor /= 10

        return new_A

def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    example_input = [1, 20, 80, 103, 130, 123456, 1234567890]

    for number in example_input:
        result = Solution().randomize_solution1(number)
        print("%s ==> %s" % (number, result))

    # lines = readlines()
    # while True:
    #     try:
    #         line = lines.next()
    #         line = line.strip()
    #         number = int(line)
    #         result = Solution().randomize_solution2(number)
    #         print("%s ==> %s" % (number, result))
    #     except StopIteration:
    #         break


if __name__ == '__main__':
    main()
