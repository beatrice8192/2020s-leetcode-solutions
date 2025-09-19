# https://leetcode.com/problems/excel-sheet-column-number
class Solution(object):
    # def titleToNumber(self, columnTitle: str) -> int:
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        if (len(columnTitle) == 0):
            return 0
        else:
            return 26 * self.titleToNumber(columnTitle[:-1]) + ord(columnTitle[-1]) - 64

