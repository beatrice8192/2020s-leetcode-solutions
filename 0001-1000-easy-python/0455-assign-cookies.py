# https://leetcode.com/problems/assign-cookies
class Solution(object):
    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        gi = 0
        si = 0
        while (gi < len(g) and si < len(s)):
            if (g[gi] <= s[si]):
                gi += 1
            si += 1
        return gi

