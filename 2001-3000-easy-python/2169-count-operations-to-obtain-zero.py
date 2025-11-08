# https://leetcode.com/problems/count-operations-to-obtain-zero
class Solution(object):
    # def countOperations(self, num1: int, num2: int) -> int:
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        result = 0
        while (num1 != 0 and num2 != 0):
            if (num1 >= num2):
                result += int(num1 / num2)
                num1 %= num2
            else:
                result += int(num2 / num1)
                num2 %= num1
        return result

