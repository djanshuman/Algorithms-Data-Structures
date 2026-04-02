'''
https://leetcode.com/problems/largest-rectangle-in-histogram/

Current:Array/Stack/Monotonic Stack
Key Idea:Identifying the nearest smaller neighbors to calculate the maximum width for each bar acting as the minimum height.
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #monotonically increasing heights
        max_area = 0
        heights = heights + [0] # adding a fake bar / sentinel element at the end to ensure all bars are calculated.
        

        for i , n in enumerate(heights):
            while stack and heights[stack[-1]] > n:
                height = heights[stack.pop()]
                width = i if not stack else (i - stack[-1] - 1)
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
        
