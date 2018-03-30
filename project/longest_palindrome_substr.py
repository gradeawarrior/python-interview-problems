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
        palindromes = []

        # Counting letters for better optimizations
        letter_count = {}
        for letter in s:
            if letter in letter_count: letter_count[letter] += 1
            else: letter_count[letter] = 1
        multiple_letters = [letter for letter in letter_count if letter_count[letter] > 1]
        three_or_more_letters = [letter for letter in letter_count if letter_count[letter] >= 3]
        if config.debug: print("multiple_letters: %s" % multiple_letters)

        # 4-character palindromes
        for letter in multiple_letters:
            for mletter in multiple_letters:
                if letter == mletter and letter_count[letter] < 4: continue
                potential = mletter + letter + letter + mletter
                if potential in s and potential not in palindromes:
                    if len(potential) > len(longest): longest = potential
                    palindromes.append(potential)
        if config.debug: print("palindromes: %s" % palindromes)

        # basic 3-character palindromes
        for letter in letter_count:
            for mletter in multiple_letters:
                if letter == mletter and letter_count[letter] < 3: continue
                potential = mletter + letter + mletter
                if potential in s:
                    if len(potential) > len(longest): longest = potential
                    palindromes.append(potential)
        if config.debug: print("palindromes: %s" % palindromes)


        # Simple palindromes
        for letter in multiple_letters:
            if config.debug: print("< letter: %s - count: %s" % (letter, letter_count[letter]))
            potential = letter + letter
            for i in xrange(1, letter_count[letter]):
                if config.debug: print("> letter: %s potential: '%s' - i: %s - count: %s"
                        % (letter, potential, i, letter_count[letter]))
                if len(potential) >= len(longest) and potential in s:
                    longest = potential
                potential += letter
        if config.debug: print("longest: %s" % longest)

        # If no palindromes are detected, return immediately
        if not palindromes and len(longest) <= 2: return longest

        middle_idx = len(s)/2-1 if len(s) % 2 == 0 else len(s)/2
        for palindrome in palindromes:
            # Search for larger palindromes
            start_idx = s.find(palindrome)
            while start_idx != -1:
                idx1, idx2 = start_idx-1, start_idx+len(palindrome)
                if config.debug:
                    print("palindrome: '%s' - start_idx: %s - s[%s:%s]" %
                            (palindrome, start_idx, idx1, idx2))

                # Build upon known palindromes
                while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
                    current = s[idx1:idx2+1]
                    if config.debug: print("  -> current: '%s' - s[%s:%s]" % (current, idx1, idx2))
                    if len(current) > len(longest):
                        if config.debug: print("New longest: '%s'" % current)
                        longest = current
                    idx1 -= 1
                    idx2 += 1
                start_idx += 1
                start_idx = s.find(palindrome, start_idx)

        # Deal with situations when length == 3, find the first occurence
        if len(longest) == 3 or len(longest) == 4:
            for k in xrange(0, len(palindromes)-1):
                if len(palindromes[k]) < len(longest): continue
                idx1 = s.find(palindromes[k])
                for l in xrange(1, len(palindromes)):
                    if len(palindromes[l]) < len(longest): continue
                    idx2 = s.find(palindromes[l])
                    if idx1 <= idx2: longest = palindromes[k]
                    else:            longest = palindromes[l]

        if config.debug: print("longest: '%s'" % longest)
        return longest

    def longestPalindromeBruteForce(self, s):
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

