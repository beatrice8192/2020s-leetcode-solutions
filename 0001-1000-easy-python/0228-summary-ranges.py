# https://leetcode.com/problems/summary-ranges
class Solution(object):
    # def summaryRanges(self, nums: List[int]) -> List[str]:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if (len(nums) == 0):
            return []
        ranges = [(nums[0], nums[0])]
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1] > 1):
                ranges[-1] = (ranges[-1][0], nums[i-1])
                ranges.append((nums[i], nums[i]))
        ranges[-1] = (ranges[-1][0], nums[-1])
        return [(str(x[0]) if (x[0] == x[1]) else ("%d->%d" % (x[0], x[1]))) for x in ranges]

