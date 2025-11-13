# https://leetcode.com/problems/number-of-lines-to-write-string
class Solution(object):
    # def numberOfLines(self, widths: List[int], s: str) -> List[int]:
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines = 1
        length = 0
        def getWidth(char):
            return widths[ord(char) - 97]
        for char in s:
            length += getWidth(char)
            if (length > 100):
                lines += 1
                length = getWidth(char)
        return [lines, length]

