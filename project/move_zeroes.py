class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        while p1 < len(nums):
            # Find me my 0
            while (p1 < len(nums) and nums[p1] != 0): p1 += 1
            # Find me non-zero
            while (p2 < len(nums) and (nums[p2] == 0 or p2 < p1)): p2 += 1

            # switch values
            if p2 >= len(nums): break
            nums[p1] = nums[p2]
            nums[p2] = 0

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)

            ret = Solution().moveZeroes(nums)

            out = integerListToString(nums)
            if ret is not None:
                print "Do not return anything, modify nums in-place instead."
            else:
                print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
