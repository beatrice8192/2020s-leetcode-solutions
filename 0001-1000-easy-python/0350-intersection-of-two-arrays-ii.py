# https://leetcode.com/problems/intersection-of-two-arrays-ii
class Solution(object):
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map1 = {}
        intersection = []
        for n in nums1:
            if (n not in map1):
                map1[n] = 0
            map1[n] += 1
        for n in nums2:
            if (n in map1 and map1[n] > 0):
                map1[n] -= 1
                intersection.append(n)
        return intersection

