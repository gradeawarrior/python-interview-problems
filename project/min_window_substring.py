import project.config as config

class Solution(object):
    def minWindow(self, s, t):
        """
        Given a string S and a string T, find the minimum window in S
        which will contain all the characters in T in complexity O(n)
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0 or len(t) == 0 or len(s) < len(t): return ""

        strarray = [letter for letter in t]
        ptr1 = 0
        ptr2 = len(t)

        # Set initial expectations
        current = s[ptr1:ptr2]
        for index, letter in enumerate(current):
            if letter in strarray: strarray.remove(letter)
            elif letter not in strarray and letter in t:
                ptr1 = index
        if len(strarray) == 0: return current

        ptr2 += 1
        new_ptr = True
        window = ""
        while ptr2 <= len(s):
            current = s[ptr1:ptr2]
            if config.debug: print("%s - %s:%s - %s" % (current, ptr1, ptr2, strarray))
            if s[ptr2-1] in strarray:
                strarray.remove(s[ptr2-1])
            elif new_ptr and s[ptr2-1] in t:
                while s[ptr2-1] not in strarray:
                    if config.debug: print("s[%s] = %s" % (ptr1, s[ptr1]))
                    if s[ptr1] == s[ptr2-1]:
                        ptr1 += 1
                        break
                    elif s[ptr1] in t: strarray.append(s[ptr1])
                    ptr1 += 1
                new_ptr = False
                continue
            if len(strarray) == 0:
                new_ptr = False
                # Set window if the current window is the smallest
                if not window or len(current) < len(window):
                    window = current

                # Otherwise if larger, then increase ptr1
                if len(current) >= len(window) and len(current) > len(t):
                    if config.debug: print("increase ptr1 %s ==> %s" %(ptr1, ptr1+1))
                    if s[ptr1] in t: strarray.append(s[ptr1])
                    # if s[ptr1] in t:
                    #     continue
                    # else:
                    ptr1 += 1
                    continue

                # Quit immediately if I've already met the requirements
                if len(window) == len(t): break

            elif ptr2 < len(s):
                ptr2 += 1
                new_ptr = True
            else:
                break
        return window

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            line = lines.next()
            t = stringToString(line)

            ret = Solution().minWindow(s, t)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
