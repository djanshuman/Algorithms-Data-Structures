'''
https://leetcode.com/problems/contains-duplicate/description/
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset =set()

        for i in nums:
            if i in myset:
                return True
            myset.add(i)
        return False

        
