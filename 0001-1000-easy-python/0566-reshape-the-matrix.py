# https://leetcode.com/problems/reshape-the-matrix
class Solution(object):
    # def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if (len(mat) * len(mat[0]) != r * c):
            return mat
        flattened = [cell for row in mat for cell in row]
        return [flattened[i:(i+c)] for i in range(0, len(flattened), c)]

