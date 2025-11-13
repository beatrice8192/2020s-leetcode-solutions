# https://leetcode.com/problems/longest-harmonious-subsequence
class Solution(object):
    # def findLHS(self, nums: List[int]) -> int:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        map = {}
        for n in nums:
            if (n not in map):
                map[n] = 0
            map[n] += 1
        keys = sorted(map.keys())
        for i in range(1, len(keys)):
            if (keys[i-1] + 1 == keys[i]):
                result = max(result, map[keys[i-1]] + map[keys[i]])
        return result

