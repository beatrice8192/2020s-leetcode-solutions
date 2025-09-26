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
        result = [""] * numRows
        for i in range(len(s)):
            if (i % loop_size < numRows):
                result[i % loop_size] += s[i]
            else:
                result[loop_size - i % loop_size] += s[i]
        return "".join(result)

