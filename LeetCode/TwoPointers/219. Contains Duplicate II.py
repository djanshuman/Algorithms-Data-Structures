'''
https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myset = set()
        l = 0

        for r in range(len(nums)):
            ele = nums[r]

            #1. Window shifting
            if abs(r - l) > k:
                myset.remove(nums[l])
                l += 1
            #2. Check dups. if dups check is happening means we are within valid window. 
            if ele in myset:
                return True
            myset.add(ele)

        return False


    
