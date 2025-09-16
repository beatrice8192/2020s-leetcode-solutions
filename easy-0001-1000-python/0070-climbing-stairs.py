# https://leetcode.com/problems/climbing-stairs
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1*45 + 2*0 = c(45,0)

        # 1*43 + 2*1 = c(44,1)
        # (44)/(1) = previous/45*45*44/1

        # 1*41 + 2*2 = c(43,2)
        # (43*42)/(2*1) = previous/44*43*42/2

        # 1*39 + 2*3 = c(42,3)
        # (42*41*40)/(3*2*1) = previous/43*41*40/3

        # 1*3 + 2*21 = c(24,21)
        # previous/25*5*4/21

        # 1*1 + 2*22 = c(23,22)
        # previous/24*3*2/22
        ones = n
        twos = 0
        total = 1
        combination = 1
        while ones >= 2:
            ones -= 2
            twos += 1
            combination *= (ones + 1) * (ones + 2)
            combination /= (ones + twos + 1) * (twos)
            # print ones, twos, combination
            total += combination
        return total

