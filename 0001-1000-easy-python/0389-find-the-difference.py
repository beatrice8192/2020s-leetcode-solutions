# https://leetcode.com/problems/find-the-difference
class Solution(object):
    # def findTheDifference(self, s: str, t: str) -> str:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map = {}
        for char in s:
            if (char not in map):
                map[char] = 0
            map[char] += 1
        for char in t:
            if (char not in map or map[char] == 0):
                return char
            map[char] -= 1
        return None

