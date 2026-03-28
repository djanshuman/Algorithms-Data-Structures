'''
https://leetcode.com/problems/contiguous-array/description/
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_map = {0:-1}
        current_sum = 0
        max_len = 0

        for i , e in enumerate(nums):
            if e == 1:
                current_sum += 1
            else:
                current_sum -= 1
            
            if current_sum in prefix_map:
                start_idx = prefix_map[current_sum]
                max_len = max(max_len,i - start_idx)
                
            else:
                prefix_map[current_sum] = i
        return max_len
