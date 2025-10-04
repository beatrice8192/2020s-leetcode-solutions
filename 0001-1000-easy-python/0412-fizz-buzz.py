# https://leetcode.com/problems/fizz-buzz
class Solution(object):
    # def fizzBuzz(self, n: int) -> List[str]:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = [""] * n
        for i in range(n):
            if ((i + 1) % 3 == 0):
                result[i] += "Fizz"
            if ((i + 1) % 5 == 0):
                result[i] += "Buzz"
            if (result[i] == ""):
                result[i] = str(i + 1)
        return result

