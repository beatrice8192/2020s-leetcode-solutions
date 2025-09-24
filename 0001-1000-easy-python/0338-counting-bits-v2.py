# https://leetcode.com/problems/counting-bits

# observe the patterns:
# 0       0
# 1       1
# 10      1
# 11      2
# 100     1 [x + 1 for x in previous 4]
# 101     2
# 110     2
# 111     3
# 1000    1 [x + 1 for x in previous 8]
# 1001    2
# 1010    2
# 1011    3
# 1100    2
# 1101    3
# 1110    3
# 1111    4
# 10000   1 [x + 1 for x in previous 16]
# 10001   2
# 10010   2
# 10011   3
# 10100   2
# 10101   3
# 10110   3
# 10111   4
# 11000   2
# 11001   3
# 11010   3
# 11011   4
# 11100   3
# 11101   4
# 11110   4
# 11111   5

class Solution(object):
    # def countBits(self, n: int) -> List[int]:
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        while (len(result) < n + 1):
            result.extend([(x + 1) for x in result])
        return result[:(n + 1)]

