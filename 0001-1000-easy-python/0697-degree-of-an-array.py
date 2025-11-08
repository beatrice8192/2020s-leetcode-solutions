# https://leetcode.com/problems/degree-of-an-array
class Solution(object):
    # def findShortestSubArray(self, nums: List[int]) -> int:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurrences = {}
        for i in range(len(nums)):
            if (nums[i] not in occurrences):
                occurrences[nums[i]] = (1, i, i) # count, min index, max index
            else:
                occurrences[nums[i]] = (occurrences[nums[i]][0]+1, occurrences[nums[i]][1], i)
        frequencies = list(reversed(sorted(occurrences.values())))
        mode = frequencies[0]
        degree = mode[2] - mode[1] + 1
        for i in range(1, len(frequencies)):
            if (frequencies[i][0] < mode[0]):
                break
            degree = min(degree, frequencies[i][2] - frequencies[i][1] + 1)
        return degree

