"""
Given an array of integers and a partitions value, return True/False if the array can be
partitioned such that the sum of each partition equals the sum the each other.

Examples:

    A = [2, 3, 1, 4, 5]
    p = 3
    result: True because [[2, 3], [1, 4], [5]]

    A = [5, 2, 3, 1, 4]
    p = 3
    result: True because [[5], [2, 3], [1, 4]]

    A = [5, 5, 1, 2, 2]
    p = 3
    result: True because [[5], [5], [1, 2, 2]]

    A = [1, 2, 3, 4, 5]
    p = 3
    result: False
"""

import json
import project.config as config


class Solution():
    def equalPartitions(self, A, p):
        """
        :param A: A list of integers
        :param p: The partition value
        :returns: True/False if the array can be partitioned such that the sum of each partition
                  equals the some of each other
        """
        if p <= 0: raise ValueError("p must be a partition value >= 1")
        elif not A: raise ValueError("The array must not be empty")
        elif p == 1: return True
        elif p > len(A): return False

        # Calculate likelihood of a window size
        max_window_l = len(A) - (p-1)
        occurences = {}
        if config.debug:
            print("Max window: %s" % max_window_l)
            print("A: %s" % A)
        for window_l in xrange(max_window_l, 0, -1):
            idx1 = 0
            idx2 = idx1 + window_l
            while idx2 <= len(A):
                csum = sum(A[idx1:idx2])
                if csum in occurences: occurences[csum] += 1
                else:                  occurences[csum]  = 1
                idx1 += 1
                idx2 += 1
        # Create a list where the count of potential sums is >= p
        probable_sums = [psum for psum in occurences if occurences[psum] >= p]

        if config.debug:
            print(json.dumps(occurences, indent=2))
            print("Probable sums: %s" % probable_sums)

        # Knowing the distribution of potential sums, I can quickly determine True/False for 2-cases
        if len(probable_sums) == 0: return False
        if p == len(A) and len(occurences) == 1: return True

        # Attempt to generate these partitions based on probable sums
        potential_p = {}
        for esum in probable_sums:
            idx1 = 0
            idx2 = idx1 + max_window_l
            while idx2 > idx1 and idx2 <= len(A):
                csum = sum(A[idx1:idx2])
                if csum != esum:
                    idx2 -= 1
                    continue
                if csum in potential_p: potential_p[csum].append(A[idx1:idx2])
                else:                   potential_p[csum] = [A[idx1:idx2]]
                idx1 = idx2
                idx2 = idx1 + max_window_l
                if idx2 >= len(A): idx2 = len(A)
        if config.debug: print(potential_p)

        # If I have a valid partition pattern that equals p, then True; otherwise False
        return len([True for csum in potential_p if len(potential_p[csum]) == p]) >= 1

