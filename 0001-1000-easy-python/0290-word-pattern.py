# https://leetcode.com/problems/word-pattern
# referencing the solution of:
# https://leetcode.com/problems/isomorphic-strings
class Solution(object):
    # def wordPattern(self, pattern: str, s: str) -> bool:
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        else:
            return self.isIsomorphic(pattern, words)

    # def isIsomorphic(self, s: str, t: str) -> bool:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_st = {}
        map_ts = {}
        for i in range(len(s)):
            if (s[i] in map_st and map_st[s[i]] != t[i]):
                return False
            else:
                map_st[s[i]] = t[i]
            if (t[i] in map_ts and map_ts[t[i]] != s[i]):
                return False
            else:
                map_ts[t[i]] = s[i]
        return True

