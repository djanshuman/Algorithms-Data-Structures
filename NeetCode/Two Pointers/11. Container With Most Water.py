'''
https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150
https://leetcode.com/problems/container-with-most-water/description/
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = (r - l) * min(height[l],height[r])
            max_area = max(area,max_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
