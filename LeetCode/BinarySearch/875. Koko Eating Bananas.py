'''
https://leetcode.com/problems/koko-eating-bananas/
'''
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = -1

        while(low <= high):
            mid = (low+high) // 2
            if self.feasible_solution(piles,h,mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def feasible_solution(self,piles,h,k):
        num_hours = 0

        for p in piles:
            num_hours += math.ceil(p/k)
        
        return num_hours <= h
