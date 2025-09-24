# https://leetcode.com/problems/reverse-vowels-of-a-string
class Solution(object):
    VOWELS = ['a', 'e', 'i', 'o', 'u']

    # def reverseVowels(self, s: str) -> str:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = len(s) - 1
        array = list(s)
        while (True):
            while (start < len(s) and lower(s[start]) not in self.VOWELS):
                start += 1
            while (end > start and lower(s[end]) not in self.VOWELS):
                end -= 1
            if (start < end):
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1
            else:
                break
        return ''.join(array)

