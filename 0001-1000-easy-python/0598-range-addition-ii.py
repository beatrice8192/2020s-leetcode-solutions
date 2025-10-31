# https://leetcode.com/problems/range-addition-ii
class Solution(object):
    # def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if (len(ops) == 0):
            return m * n
        else:
            return min([o[0] for o in ops]) * min([o[1] for o in ops])

