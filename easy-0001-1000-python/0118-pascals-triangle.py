# https://leetcode.com/problems/pascals-triangle
class Solution(object):
    # def generate(self, numRows: int) -> List[List[int]]:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        return [self.getRow(row) for row in range(numRows)]

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

