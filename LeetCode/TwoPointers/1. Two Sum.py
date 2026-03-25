'''
https://leetcode.com/problems/two-sum/description/
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        myDict= dict()

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in myDict:
                return [myDict[compliment], i]
            myDict[nums[i]] = i 

        return []
