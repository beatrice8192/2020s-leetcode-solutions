# https://leetcode.com/problems/intersection-of-two-arrays
class Solution(object):
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map1 = {}
        intersection = {}
        for n in nums1:
            map1[n] = True
        for n in nums2:
            if (n in map1):
                intersection[n] = True
        return intersection.keys()

