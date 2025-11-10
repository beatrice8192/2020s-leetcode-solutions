# https://leetcode.com/problems/min-cost-climbing-stairs
class Solution(object):
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp_result = [0] * len(cost)
        for i in range(2, len(cost)):
            dp_result[i] = min(dp_result[i-1] + cost[i-1], dp_result[i-2] + cost[i-2])
        return min(dp_result[-1] + cost[-1], dp_result[-2] + cost[-2])

