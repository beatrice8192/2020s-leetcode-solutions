# https://leetcode.com/problems/positions-of-large-groups
class Solution(object):
    # def largeGroupPositions(self, s: str) -> List[List[int]]:
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        while (i < len(s)):
            j = i
            while (i < len(s) and s[i] == s[j]):
                i += 1
            if (i - j > 2):
                result.append([j, i - 1])
        return result

