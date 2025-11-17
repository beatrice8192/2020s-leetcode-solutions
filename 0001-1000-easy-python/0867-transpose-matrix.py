# https://leetcode.com/problems/transpose-matrix
class Solution(object):
    # def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        columns = len(matrix[0])
        return [[matrix[r][c] for r in range(rows)] for c in range(columns)]

