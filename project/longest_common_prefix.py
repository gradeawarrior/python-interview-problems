"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""
import project.config as config


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        elif len(strs) == 1: return strs[0]

        # Set result to the shortest str in the list
        result = strs[0]
        for idx in xrange(1, len(strs)):
            if len(strs[idx]) < len(result): result = strs[idx]

        # Find a pattern between each word
        for idx in xrange(0, len(strs)):
            if result == strs[idx]: continue

            # Find the smallest common window between each word
            window_l = len(result)
            for width in xrange(window_l, 0, -1):
                substr = strs[idx][0:width]
                if config.debug: print("result: '%s' - substr: '%s' width: %s" %
                        (result, substr, width))
                if substr in result:
                    if substr == result[0:width]:
                        result = substr
                        break
                elif width == 1:
                    result = ""
                else:
                    result = result[0:width]

            # If I find that there is no common window, then quit trying to check immediately
            if not result: break

        if config.debug: print("result: '%s'" % result)
	return result

