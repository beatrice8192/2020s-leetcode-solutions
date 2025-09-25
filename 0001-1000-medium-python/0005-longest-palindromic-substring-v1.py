# https://leetcode.com/problems/longest-palindromic-substring
class Solution(object):
    # def longestPalindrome(self, s: str) -> str:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        map = {}
        max_len = 1
        max_start = 0
        for i in range(len(s)):
            if (s[i] not in map):
                # keep track of indexes of every char
                map[s[i]] = [i]
            else:
                # found repeating char, might be palindrome
                for start in map[s[i]]:
                    left = start
                    right = i
                    current_len = i - start + 1
                    if (current_len <= max_len):
                        break
                    while (left < right and s[left] == s[right]):
                        left += 1
                        right -= 1
                    if (s[left] == s[right]):
                        # found longest palindrome ending with i, stop checking the rest of start
                        max_len = current_len
                        max_start = start
                        break
                map[s[i]].append(i)
        return s[max_start:(max_start + max_len)]

