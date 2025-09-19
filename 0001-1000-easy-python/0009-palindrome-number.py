# https://leetcode.com/problems/palindrome-number
class Solution(object):
    # sys.maxsize
    MAXSIZE = 2 ** 31

    # def isPalindrome(self, x: int) -> bool:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        y = x
        reverse = y % 10
        while (y >= 10):
            y = int(y / 10)
            reverse = self.add(reverse, y % 10)
            if (reverse < 0):
                return False
        return reverse == x

    # def add(self, tens: int, ones: int) -> int:
    def add(self, tens, ones):
        if ((tens < self.MAXSIZE / 10) or \
            (tens == self.MAXSIZE / 10 and ones < self.MAXSIZE % 10)):
            return tens * 10 + ones
        else:
            return -1

