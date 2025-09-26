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
        result = [""] * numRows
        row = 0
        direction = 1 # 1 = going down, -1 = going up
        for char in s:
            result[row] += char
            row += direction
            if (row == numRows - 1):
                direction = -1
            elif (row == 0):
                direction = 1
        return "".join(result)

