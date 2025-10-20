# https://leetcode.com/problems/final-value-of-variable-after-performing-operations
class Solution(object):
    # def finalValueAfterOperations(self, operations: List[str]) -> int:
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        return len([x for x in operations if x[1] == "+"]) - len([x for x in operations if x[1] == "-"])

