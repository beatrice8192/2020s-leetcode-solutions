# https://leetcode.com/problems/is-subsequence
class Solution(object):
    # def isSubsequence(self, s: str, t: str) -> bool:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) > len(t)):
            return False
        si = 0
        ti = 0
        while (si < len(s) and ti < len(t)):
            if (s[si] == t[ti]):
                si += 1
            ti += 1
        return si == len(s)

