# https://leetcode.com/problems/guess-number-higher-or-lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    # def guessNumber(self, n: int) -> int:
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while (start <= end):
            mid = int((start + end) / 2)
            mid_guess = guess(mid)
            if (mid_guess == -1):
                end = mid - 1
            elif (mid_guess == 1):
                start = mid + 1
            else:
                return mid

