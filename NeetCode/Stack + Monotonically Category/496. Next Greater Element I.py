'''
https://leetcode.com/problems/next-greater-element-i/description/
'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}  #monotonically increasing sequence
        stack = []

        for i , n in enumerate(nums2):
            while stack and nums2[stack[-1]] < n:
                idx = stack.pop()
                res[nums2[idx]] = n
            stack.append(i)
        
        return [res.get(x,-1) for x in nums1]
