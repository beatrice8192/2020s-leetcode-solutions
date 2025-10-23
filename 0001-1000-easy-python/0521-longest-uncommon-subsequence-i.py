# https://leetcode.com/problems/longest-uncommon-subsequence-i
class Solution(object):
    # def findLUSlength(self, a: str, b: str) -> int:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if (a == b) else max(len(a), len(b))

