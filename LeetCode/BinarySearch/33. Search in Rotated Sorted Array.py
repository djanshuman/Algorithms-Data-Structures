'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while(left <= right):
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # check if mid is in left hump
            if nums[mid] > nums[-1]:

                if target > nums[mid]:
                    left = mid + 1

                elif target <= nums[-1]:
                    left = mid + 1

                else:
                    right = mid - 1
                
            # check if mid is in right hump
            else:
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[-1]:
                    right = mid - 1
                else:
                    left = mid + 1
        return - 1

