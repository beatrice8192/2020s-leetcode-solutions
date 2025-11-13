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
        for i in range(1, len(timeSeries)):
            result += min(duration, timeSeries[i] - timeSeries[i-1])
        return result + duration

