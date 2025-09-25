# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    # def lengthOfLongestSubstring(self, s: str) -> int:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        max_len = 0
        max_start = 0
        current_len = 0
        current_start = 0
        for i in range(len(s)):
            if (s[i] in map):
                # duplicate
                if (current_len > max_len):
                    max_len = current_len
                    max_start = current_start
                if (map[s[i]] >= current_start):
                    current_start = map[s[i]] + 1
                    current_len = i - current_start + 1
                else:
                    current_len += 1
                map[s[i]] = i
            else:
                # not duplicate
                current_len += 1
                map[s[i]] = i
        return max(max_len, current_len)

