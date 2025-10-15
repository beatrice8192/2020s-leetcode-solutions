class Solution(object):
    # def arrangeCoins(self, n: int) -> int:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # applying quadratic formula to solve x:
        # (x + 1) * x / 2 <= n
        # x^2 + x - 2n <= 0
        # x <= (-1 + (1 + 8n)^0.5) / 2
        return int(((n * 8 + 1) ** 0.5 - 1) / 2)

