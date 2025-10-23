# https://leetcode.com/problems/student-attendance-record-i
class Solution(object):
    # def checkRecord(self, s: str) -> bool:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count("A") < 2 and "LLL" not in s

