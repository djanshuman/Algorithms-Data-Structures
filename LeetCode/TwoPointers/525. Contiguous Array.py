'''
https://leetcode.com/problems/contiguous-array/description/
'''

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        # Step 1: Initialize (Value: Index)
        # We saw a sum of 0 at the "starting line" (index -1)
        prefix_map = {0: -1}
        current_sum = 0
        max_len = 0
        
        for i, num in enumerate(nums):
            # Step 2: Transform 0 to -1 on the fly
            if num == 1:
                current_sum += 1
            else:
                current_sum -= 1
            
            # Step 3: Check if we've seen this sum before
            if current_sum in prefix_map:
                # Calculate the distance from the FIRST time we saw this sum
                start_index = prefix_map[current_sum]
                max_len = max(max_len, i - start_index)
            else:
                # Stay Left Rule: Only record the index the FIRST time
                prefix_map[current_sum] = i
                
        return max_len
