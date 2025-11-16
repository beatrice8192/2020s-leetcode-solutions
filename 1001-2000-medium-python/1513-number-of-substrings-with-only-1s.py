# https://leetcode.com/problems/number-of-substrings-with-only-1s
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        count = 0
        i = 0
        while (i < len(s)):
            while (i < len(s) and s[i] == "0"):
                i += 1
            j = i
            while (i < len(s) and s[i] == "1"):
                i += 1
            count = (count + int((i - j) * (i - j + 1) / 2)) % MOD
        return count

