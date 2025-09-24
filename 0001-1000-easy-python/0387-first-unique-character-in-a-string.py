# https://leetcode.com/problems/first-unique-character-in-a-string
class Solution(object):
    # def firstUniqChar(self, s: str) -> int:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        indexes = {}
        for i in range(len(s)):
            if (s[i] not in indexes):
                indexes[s[i]] = i
            else:
                indexes[s[i]] = -1
        indexes = [x for x in indexes.values() if x != -1]
        return -1 if (len(indexes) == 0) else min(indexes)

