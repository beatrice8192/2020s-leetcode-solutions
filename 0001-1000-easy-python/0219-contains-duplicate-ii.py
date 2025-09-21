# https://leetcode.com/problems/contains-duplicate-ii
class Solution(object):
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {}
        for i in range(len(nums)):
            if (nums[i] in map and i - map[nums[i]] <= k):
                return True
            else:
                map[nums[i]] = i
        return False

