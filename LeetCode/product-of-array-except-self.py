"""
https://leetcode.com/problems/product-of-array-except-self/description/
"""

class Solution(object):
    def productExceptSelf(self, nums):
        result_list = [0] * len(nums)
        prefix = 1

        # prefix calculation O(n)
        for i in range(len(nums)):
            result_list[i] = prefix
            prefix = prefix * nums[i]

        # postfix calculation # [1, 1, 2, 6]
        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            result_list[j] *= postfix
            postfix = nums[j] * postfix
        return result_list
