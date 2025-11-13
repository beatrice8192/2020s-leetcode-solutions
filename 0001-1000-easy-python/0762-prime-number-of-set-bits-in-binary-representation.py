# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # The prime number set that 2^x <= 10^6
        prime = set([2,3,5,7,11,13,17,19,23])
        return len([num for num in range(left, right+1) if num.bit_count() in prime])

