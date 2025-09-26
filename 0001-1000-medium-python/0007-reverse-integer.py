class Solution(object):
    # def reverse(self, x: int) -> int:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        positive = (x == abs(x))
        x = abs(x)
        while (x > 0):
            result = result * 10 + x % 10
            x = int(x / 10)
        if (result > 2 ** 31 - 1):
            return 0
        return result if positive else -result

