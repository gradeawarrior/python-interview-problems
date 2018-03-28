"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0

Example 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5

Example 3:

    nums1 = [1, 3]
    nums2 = [2, 4]

    The median is (2 + 3)/2 = 2.5
"""

import project.config as config

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums1_mid = nums1_len/2
        nums2_len = len(nums2)
        nums2_mid = nums2_len/2
        middle = []

        # If both lists are empty
        if nums1_len == 0 and nums2_len == 0: return 0.0

        # If one of the lists are empty
        elif nums2_len == 0:
            if nums1_len % 2 == 1: return float(nums1[nums1_mid])
            else: return (nums1[nums1_mid-1] + nums1[nums1_mid])/2.0
        elif nums1_len == 0:
            if nums2_len % 2 == 1: return float(nums2[nums2_mid])
            else: return (nums2[nums2_mid-1] + nums2[nums2_mid])/2.0

        # Most cases where both lists have items
        else:
            larger_l = nums1 if nums1_len > nums2_len else nums2
            smaller_l = nums1 if nums1_len <= nums2_len else nums2
            if config.debug: print("larger_l: %s - smaller_l: %s" % (larger_l, smaller_l))

            # Add smaller list into larger list, while calculating middle
            for number in smaller_l:
                # Get middle
                if len(larger_l) % 2 == 0:
                    mid_idx = len(larger_l)/2 - 1
                    middle = [larger_l[mid_idx], larger_l[mid_idx+1]]
                else:
                    mid_idx= len(larger_l)/2
                    middle = [larger_l[mid_idx]]
                if config.debug:
                    print("list: %s - current middle: %s - number: %s" % (larger_l, middle, number))

                # If current length of larger_l is an odd number (e.g. 1, 3, 5)
                if len(middle) == 1:
                    assert len(middle) == 1, "Expecting that middle has 1 number"
                    if number == middle[0]:
                        middle = middle[middle[0], number]
                        left = larger_l[0:mid_idx+1]
                        left.append(number)
                        right = larger_l[mid_idx+1:len(larger_l)]
                        larger_l = left + right
                    elif number < middle[0]:
                        idx = mid_idx
                        while idx >= 0:
                            if number >= larger_l[idx] :
                                left = larger_l[0:idx+1]
                                left.append(number)
                                right = larger_l[idx+1:len(larger_l)]
                                larger_l = left + right
                                break
                            elif idx == 0:
                                left = [number]
                                larger_l = left + larger_l
                                break
                            idx -= 1
                        middle = [larger_l[mid_idx], middle[0]]
                    elif number > middle[0]:
                        if config.debug: print("%s > %s (middle)" % (number, middle[0]))
                        idx = mid_idx
                        while idx < len(larger_l):
                            if number <= larger_l[idx]:
                                left = larger_l[0:idx]
                                left.append(number)
                                right = larger_l[idx:len(larger_l)]
                                larger_l = left + right
                                break
                            elif idx == len(larger_l)-1:
                                larger_l.append(number)
                                break
                            idx += 1
                        middle = [middle[0], larger_l[mid_idx+1]]
                    else:
                        raise RuntimeError("The code should never hit this")

                # If current length of larger_l is an even number (e.g. 2, 4 , 6)
                else:
                    assert len(middle) == 2, "Expecting that middle has two numbers"
                    if number == middle[0]:
                        middle = [middle[0]]
                        left = larger_l[0:mid_idx+1]
                        left.append(number)
                        right = larger_l[mid_idx+1:len(larger_l)]
                        larger_l = left + right
                    elif number == middle[1]:
                        middle = [middle[1]]
                        left = larger_l[0:mid_idx+2]
                        left.append(number)
                        right = larger_l[mid_idx+2:len(larger_l)]
                        larger_l = left + right
                    elif number < middle[0]:
                        if config.debug: print("%s < %s (middle)" % (number, middle[0]))
                        middle = [middle[0]]
                        idx = mid_idx
                        while idx >= 0:
                            if number >= larger_l[idx] :
                                left = larger_l[0:idx+1]
                                left.append(number)
                                right = larger_l[idx+1:len(larger_l)]
                                larger_l = left + right
                                break
                            elif idx == 0:
                                left = [number]
                                larger_l = left + larger_l
                                break
                            idx -= 1
                    elif number > middle[0] and number <= middle[1]:
                        if config.debug: print("%s < %s <= %s" % (middle[0], number, middle[1]))
                        middle = [number]
                        left = larger_l[0:mid_idx+1]
                        left.append(number)
                        right = larger_l[mid_idx+1:len(larger_l)]
                        larger_l = left + right
                    elif number > middle[1]:
                        if config.debug: print("%s > %s (middle)" % (number, middle[1]))
                        middle = [middle[1]]
                        idx = mid_idx
                        while idx < len(larger_l):
                            if number <= larger_l[idx]:
                                left = larger_l[0:idx]
                                left.append(number)
                                right = larger_l[idx:len(larger_l)]
                                larger_l = left + right
                                break
                            elif idx == len(larger_l)-1:
                                larger_l.append(number)
                                break
                            idx += 1
                    else:
                        raise RuntimeError("The code should never hit this")
            if config.debug: print("list: %s - middle: %s" % (larger_l, middle))
            return sum(middle)/float(len(middle))


