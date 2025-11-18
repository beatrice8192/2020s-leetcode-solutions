# https://leetcode.com/problems/fair-candy-swap
class Solution(object):
    # def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        aSum = sum(aliceSizes)
        bSum = sum(bobSizes)
        target = int((aSum + bSum) / 2)
        need = set()
        for a in aliceSizes:
            need.add(a + target - aSum)
        for b in bobSizes:
            if (b in need):
                return [b + target - bSum, b]
        return None

