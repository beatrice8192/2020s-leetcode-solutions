# https://leetcode.com/problems/pascals-triangle-ii
class Solution(object):
    # def getRow(self, rowIndex: int) -> List[int]:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        value = 1
        result = [1] * (rowIndex + 1)
        for column in range(1, rowIndex + 1):
            # calculate combination
            value *= (rowIndex + 1 - column)
            value /= (column)
            result[column] = int(value)
        return result

