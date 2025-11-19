# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards
import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        occurrences = {}
        for x in deck:
            if (x not in occurrences):
                occurrences[x] = 0
            occurrences[x] += 1
        return math.gcd(*occurrences.values()) > 1

