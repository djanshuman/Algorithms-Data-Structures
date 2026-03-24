'''
https://leetcode.com/problems/koko-eating-bananas/
'''
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        ans = -1

        while(left <= right):
            mid = (left + right) // 2
            if self.isFeasible(piles,h,mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def isFeasible(self,piles,h,k):
        num_hours = 0

        for p in piles:
            num_hours += math.ceil(p/k)
        return num_hours <= h
