# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        matches = {}
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and i <= len(haystack) - len(needle):
                matches[i] = 0
            for k in matches.keys():
                if haystack[i] == needle[matches[k]]:
                    matches[k] += 1
                    if matches[k] == len(needle):
                        return k
                else:
                    del matches[k]
        return -1

