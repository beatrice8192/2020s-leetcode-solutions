# https://leetcode.com/problems/shortest-distance-to-a-character
class Solution(object):
    # def shortestToChar(self, s: str, c: str) -> List[int]:
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        result = [0] * len(s)
        dist = sys.maxsize
        for i in range(len(s)):
            if (s[i] == c):
                dist = 0
            else:
                dist += 1
                result[i] = dist
        for i in reversed(range(len(s))):
            if (result[i] == 0):
                dist = 0
            else:
                dist += 1
                result[i] = min(result[i], dist)
        return result

