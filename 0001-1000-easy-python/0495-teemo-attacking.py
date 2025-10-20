# https://leetcode.com/problems/teemo-attacking
class Solution(object):
    # def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        result = 0
        for i in range(len(timeSeries) - 1):
            result += min(duration, timeSeries[i+1] - timeSeries[i])
        return result + duration

