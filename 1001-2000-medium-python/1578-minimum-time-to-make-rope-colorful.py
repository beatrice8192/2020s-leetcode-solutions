# https://leetcode.com/problems/minimum-time-to-make-rope-colorful
class Solution(object):
    # def minCost(self, colors: str, neededTime: List[int]) -> int:
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        result = 0
        i = 0
        while (i < len(colors)):
            j = i
            while (i < len(colors) and colors[i] == colors[j]):
                i += 1
            if (j + 1 < i):
                result += sum(neededTime[j:i]) - max(neededTime[j:i])
        return result

