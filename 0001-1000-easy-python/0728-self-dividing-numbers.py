# https://leetcode.com/problems/self-dividing-numbers
class Solution(object):
    results = {}

    # def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def selfDividing(number):
            n = number
            while (n > 0):
                if (n % 10 == 0 or number % (n % 10) != 0):
                    return False
                else:
                    n = int(n / 10)
            return True
        for i in range(left, right + 1):
            if (i not in self.results):
                self.results[i] = selfDividing(i)
        return [i for i in range(left, right + 1) if self.results[i]]

