# https://leetcode.com/problems/longest-common-prefix
class Solution(object):
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 1):
            return strs[0]
        index = 0
        while (True):
            if (index == len(strs[0])):
                return strs[0][0:index]
            for i in range(1, len(strs)):
                if (index == len(strs[i])):
                    return strs[0][0:index]
                elif (strs[i][index] != strs[0][index]):
                    return strs[0][0:index]
            index += 1
        return None

