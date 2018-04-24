"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which
has the largest sum and return its sum.

Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer
approach, which is more subtle.
"""


class Solution(object):
    def maxSubArrayOptimized(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: raise ValueError()
        elif len(nums) == 1: return nums[0]
        result = max(nums)
        dp = [nums[0]]

        for i in xrange(1, len(nums)):
            dp.append(nums[i] + (dp[i-1] if dp[i-1] > 0 else 0))
            if dp[i] > result: result = dp[i]
        return result

    def maxSubArrayUnOptimized(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: raise ValueError()
        elif len(nums) == 1: return nums[0]
        result = max(nums)
	idx1 = 0
        while idx1 < len(nums)-1:
            idx2 = idx1 + 1
            while idx2 < len(nums):
                current = sum(nums[idx1:idx2+1])
                if current > result: result = current
                idx2 += 1
            idx1 += 1
        return result
