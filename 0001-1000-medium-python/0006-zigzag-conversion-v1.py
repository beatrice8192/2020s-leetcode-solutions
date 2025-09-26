# https://leetcode.com/problems/zigzag-conversion
class Solution(object):
    # def convert(self, s: str, numRows: int) -> str:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1 or numRows >= len(s)):
            return s
        loop_size = (numRows - 1) * 2
        result = []
        result.extend([s[i] for i in range(len(s)) if i % loop_size == 0])
        for row in range(1, numRows - 1):
            result.extend([s[i] for i in range(len(s)) if i % loop_size == row or i % loop_size == loop_size - row])
        result.extend([s[i] for i in range(len(s)) if i % loop_size == numRows - 1])
        return "".join(result)

