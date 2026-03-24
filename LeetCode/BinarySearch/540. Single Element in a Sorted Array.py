'''
https://leetcode.com/problems/single-element-in-a-sorted-array/description/
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def isFeasible(idx,nums):
            if idx == len(nums) - 1:
                return True
            #even case    
            elif (idx % 2):
                return nums[idx] != nums[idx - 1]
            #odd case
            else:
                return nums[idx] != nums[idx + 1]

        left = 0
        right = len(nums) - 1
        ans = -1 

        while(left <= right):
            mid = (left + right) // 2
            if isFeasible(mid,nums):
                ans = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        return ans


        
