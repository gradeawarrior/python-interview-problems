#!/usr/bin/env python

"""
Write a function:

def solution(A)
that, given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.
Given A = [-1, -3], the function should return 1.

Assume that:
- N is an integer within the range [1..100,000];
- each element of array A is an integer within the range [-1,000,000..1,000,000].

Complexity:
- expected worst-case time complexity is O(N);
- expected worst-case space complexity is O(N), beyond input storage
  (not counting the storage required for input arguments).
"""

def solution1(A):
    """
    Assumes A is an unsorted list and this implementation makes no attempt at pre-sorting numbers.

    :param A: List - An unsorted list of ints
    :returns: int - the smallest positive integer (greater than 0) that does not occur in A
    """
    if 1 not in A: return 1
    smallest = 100001

    for number in A:
        if number < 1 or number > 100000: continue
        nnum = number+1
        pnum = number-1 if number != 1 else nnum
        if pnum not in A and pnum < smallest:
            smallest = pnum
        elif nnum not in A and nnum < smallest:
            smallest = nnum
    for number in range(1, smallest):
        if number not in A:
            return number
    return smallest

def solution2(A):
    """
    Assumes A is an unsorted list and this implementation pre-sorts the numbers.

    :param A: List - An unsorted list of ints
    :returns: int - the smallest positive integer (greater than 0) that does not occur in A
    """
    if 1 not in A: return 1
    A.sort()
    smallest = 100001

    for number in A:
        if number < 1 or number > 100000: continue
        nnum = number+1
        pnum = number-1 if number != 1 else nnum
        if pnum not in A and pnum < smallest:
            return pnum
        elif nnum not in A and nnum < smallest:
            return nnum
    return smallest

def solution3(A):
    """
    Assumes A is an unsorted list and this implementation pre-sorts the numbers. It also attempts
    to cut the problem in half by only iterating over half the List.

    :param A: List - An unsorted list of ints
    :returns: int - the smallest positive integer (greater than 0) that does not occur in A
    """
    if 1 not in A: return 1
    A.sort()
    smallest = 100001

    # Check if all negative numbers in the list
    if A[0] < 0 and A[len(A)-1] < 0:
        return 1

    # Split list in half
    middle = len(A) // 2
    if A[middle] < 0:
        return solution2(A[middle:len(A)])
    else:
        for i in xrange(0, len(A)):
            number = A[i]
            if number <= 0 or number > 10000:
                continue
            nnum = number+1
            pnum = number-1 if number > 1 else nnum
            if pnum not in A:
                return pnum
            elif nnum not in A:
                return nnum
    return smallest

def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            line = line.strip()
            data = json.loads(line)
            result = solution2(data)
            print(result)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
