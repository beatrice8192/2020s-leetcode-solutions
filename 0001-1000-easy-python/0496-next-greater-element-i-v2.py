# https://leetcode.com/problems/next-greater-element-i
class Solution(object):
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        stack = []
        for n in reversed(nums2):
            while (stack and stack[-1] <= n):
                stack.pop()
            map[n] = stack[-1] if stack else -1
            stack.append(n)
        return [map[n] for n in nums1]

