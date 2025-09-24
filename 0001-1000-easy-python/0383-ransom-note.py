# https://leetcode.com/problems/ransom-note
class Solution(object):
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return self.findTheDifference(magazine, ransomNote) == None

    # referencing the solution of:
    # https://leetcode.com/problems/find-the-difference
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

