"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum
length of s is 1000.

Example:

    Input: "babad"
    Output: "bab"

    Note: "aba" is also a valid answer.

Example:

    Input: "cbbd"
    Output: "bb"
"""

import project.config as config

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) > 1000: raise ValueError("The string cannot be more than 1000 chars")
        if not s: return ""
        if len(s) == 1: return s

        longest = s[0]
        idx1, idx2 = 0, 1

        while idx1 < len(s)-1:
            idx2 = idx1 + 1
            if len(longest) > len(s[idx1:len(s)]): break

            calculated = ""
            while idx2 < len(s):
                current = s[idx1:idx2+1]
                middle = len(current)/2
                potential = current[0:middle]
                reverse = potential[::-1]
                current_tail = current[middle:len(current)] if len(current) % 2 == 0 \
                        else current[middle+1:len(current)]
                # if not calculated and len(current) % 2 == 0:
                #     calculated = current + current[1::-1]
                # elif not calculated:
                #     calculated = current[0:-1] + current[::-1]

                if config.debug:
                    print("(%s:%s:%s) current: '%s' calculated: %s - potential: '%s' - "
                            "reverse: '%s' - tail: '%s'"
                            % (idx1, middle, idx2, current, calculated, potential, reverse, current_tail))
                if current_tail == reverse and len(current) > len(longest):
                    if config.debug: print("New longest: '%s'" % current)
                    longest = current
                # elif len(calculated) > len(s):
                #     if config.debug: print("-- breaking early. It's impossible!")
                #     break
                idx2 += 1

            if len(longest) == len(s): break
            idx1 += 1
        if config.debug: print("Returning longest: '%s'" % longest)
        return longest

