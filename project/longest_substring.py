class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
	Find the longest substring with at most with at most two distinct letters. Return the
	length of that substring.

	:param s: String - some string
	:returns: int - The length of the longest substring with at most two distinct letters
        """
        if s and len(s) < 3: return len(s)
        if not s: return 0

        ptr1, ptr2 = 0, 2
        longest_ss = s[ptr1:ptr2]
        while ptr2 < len(s):
            current_ss = s[ptr1:ptr2]
            unique_letters = {letter for letter in current_ss}
            if  s[ptr2] in current_ss or len(unique_letters) < 2:
                current_ss += s[ptr2]
                if len(current_ss) > len(longest_ss):
                    longest_ss = current_ss
                ptr2 += 1
            else:
                ptr1 += 1
        return len(longest_ss)

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            s = stringToString(line)

            ret = Solution().lengthOfLongestSubstringTwoDistinct(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
