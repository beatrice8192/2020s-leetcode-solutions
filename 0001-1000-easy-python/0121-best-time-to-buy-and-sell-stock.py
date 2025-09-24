# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# Kadane's Algorithm
class Solution(object):
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        curr_profit = 0
        for i in range(1, len(prices)):
            curr_profit = max(0, curr_profit) + prices[i] - prices[i-1]
            max_profit = max(max_profit, curr_profit)
        return max_profit

