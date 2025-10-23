# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i
class Solution(object):
    # def hasSameDigits(self, s: str) -> bool:
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if self.isPalindrome(s):
            return True
        elif (len(s) == 3):
            return False
        else:
            new_s = ""
            for i in range(len(s) - 1):
                new_s += str((int(s[i]) + int(s[i+1])) % 10)
            return self.hasSameDigits(new_s)

    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while (left < right):
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True

