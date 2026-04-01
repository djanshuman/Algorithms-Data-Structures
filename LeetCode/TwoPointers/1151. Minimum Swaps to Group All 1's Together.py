'''
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/description/
'''

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        l = 0 
        max_ones = 0
        curr_ones = 0

        for r in range(len(data)):
            curr_ones += data[r]

            if r - l + 1 > ones:
                curr_ones -= data[l]
                l += 1

            max_ones = max(max_ones, curr_ones)
        return ones - max_ones
        
