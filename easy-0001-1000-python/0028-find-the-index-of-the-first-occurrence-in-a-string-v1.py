# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for h in range(len(haystack) - len(needle) + 1):
            n = 0
            while True:
                if haystack[h + n] != needle[n]:
                    break
                n += 1
                if n == len(needle):
                    return h
        return -1

