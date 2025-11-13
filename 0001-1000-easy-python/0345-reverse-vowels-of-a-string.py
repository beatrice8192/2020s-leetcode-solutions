# https://leetcode.com/problems/reverse-vowels-of-a-string
class Solution(object):
    # def reverseVowels(self, s: str) -> str:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        start = 0
        end = len(s) - 1
        array = list(s)
        while (True):
            while (start < len(s) and s[start].lower() not in vowels):
                start += 1
            while (end > start and s[end].lower() not in vowels):
                end -= 1
            if (start < end):
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1
            else:
                break
        return ''.join(array)

