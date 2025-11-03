# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# Kadane's Algorithm
class Solution(object):
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr_profit = 0
        max_profit = 0
        for i in range(len(prices) - 1):
            curr_profit = max(0, curr_profit) + prices[i+1] - prices[i]
            max_profit = max(max_profit, curr_profit)
        return max_profit

