'''
https://leetcode.com/problems/trapping-rain-water/description/
https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax  = height[l]
        rmax = height[r]
        res = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                lmax = max(lmax,height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax,height[r])
                res += rmax - height[r]
        return res

