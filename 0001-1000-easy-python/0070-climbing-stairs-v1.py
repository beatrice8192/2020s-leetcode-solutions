# https://leetcode.com/problems/climbing-stairs

# Thinking out aloud:
# 45 of 1 + 0 of 2 = combination(45,0)

# 43 of 1 + 1 of 2 = combination(44,1)
# (44)/(1) = previous/45*45*44/1

# 41 of 1 + 2 of 2 = combination(43,2)
# (43*42)/(2*1) = previous/44*43*42/2

# 39 of 1 + 3 of 3 = combination(42,3)
# (42*41*40)/(3*2*1) = previous/43*41*40/3

# 3 of 1 + 21 of 2 = combination(24,21)
# (24*..*4)/(21*..*1) = previous/25*5*4/21

# 1 of 1 + 22 of 2 = combination(23,22)
# (23*..*2)/(22*..*1) = previous/24*3*2/22

class Solution(object):
    # def climbStairs(self, n: int) -> int:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = n
        twos = 0
        total = 1
        combination = 1
        while (ones >= 2):
            ones -= 2
            twos += 1
            combination *= (ones + 1) * (ones + 2)
            combination /= (ones + twos + 1) * (twos)
            # print ones, twos, combination
            total += combination
        return int(total)

