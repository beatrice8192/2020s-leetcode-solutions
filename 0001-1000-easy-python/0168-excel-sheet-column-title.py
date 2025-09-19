# https://leetcode.com/problems/excel-sheet-column-title
class Solution(object):
    # def convertToTitle(self, columnNumber: int) -> str:
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while (columnNumber > 0):
            i = (columnNumber - 1) % 26
            columnNumber = int((columnNumber - i) / 26)
            result = chr(i + 65) + result
        return result

