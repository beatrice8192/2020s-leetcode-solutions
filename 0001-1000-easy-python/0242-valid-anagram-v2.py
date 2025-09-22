# https://leetcode.com/problems/valid-anagram
class Solution(object):
    # def isAnagram(self, s: str, t: str) -> bool:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        map = {}
        for char in s:
            if (char not in map):
                map[char] = 0
            map[char] += 1
        for char in t:
            if (char not in map or map[char] == 0):
                return False
            map[char] -= 1
        return True

