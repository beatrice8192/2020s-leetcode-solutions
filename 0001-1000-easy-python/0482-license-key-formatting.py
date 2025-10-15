# https://leetcode.com/problems/license-key-formatting
class Solution(object):
    # def licenseKeyFormatting(self, s: str, k: int) -> str:
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace("-", "").upper()
        result = ""
        if (len(s) % k != 0):
            result = s[:len(s) % k] + "-"
        for i in range(len(s) % k, len(s), k):
            result += s[i:(i + k)] + "-"
        return result[:-1] if len(result) > 0 else result

