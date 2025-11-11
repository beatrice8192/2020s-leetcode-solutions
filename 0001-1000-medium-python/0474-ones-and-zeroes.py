# https://leetcode.com/problems/ones-and-zeroes
# https://en.wikipedia.org/wiki/Knapsack_problem

# Thinking out aloud:
# strs = ["00","0","11","0","0","1","1","1"]
# m = 2
# n = 2

# In a matrix of i0 number of zeros and i1 number of ones,
# dp_result[i0][i1]: do not include the current string s;
# 1 + dp_result[i0 - zeros][i1 - ones]: include the current string s and increment the number of strings by 1;

# The number of zeros and ones will not overflow the constraints of m and n in the matrix
# because dp_result[i0][i1] is at most dp_result[i0 - 1][i1] + 1 or dp_result[i0][i1 - 1] + 1.

# (2, 0, [[0, 0, 0],
#         [0, 0, 0],
#         [1, 1, 1]])
# (1, 0, [[0, 0, 0],
#         [1, 1, 1],
#         [1, 1, 1]])
# (0, 2, [[0, 0, 1],
#         [1, 1, 2],
#         [1, 1, 2]])
# (1, 0, [[0, 0, 1],
#         [1, 1, 2],
#         [2, 2, 3]])
# (1, 0, [[0, 0, 1],
#         [1, 1, 2],
#         [2, 2, 3]])
# (0, 1, [[0, 1, 1],
#         [1, 2, 2],
#         [2, 3, 3]])
# (0, 1, [[0, 1, 2],
#         [1, 2, 3],
#         [2, 3, 4]])
# (0, 1, [[0, 1, 2],
#         [1, 2, 3],
#         [2, 3, 4]])

class Solution(object):
    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp_result = [[0] * (n + 1) for i in range(m + 1)]
        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros
            for i0 in range(m, zeros - 1, -1):
                for i1 in range(n, ones - 1, -1):
                    dp_result[i0][i1] = max(dp_result[i0][i1], 1 + dp_result[i0 - zeros][i1 - ones])
        return dp_result[m][n]

