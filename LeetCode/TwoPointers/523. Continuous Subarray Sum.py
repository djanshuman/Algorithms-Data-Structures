'''
https://leetcode.com/problems/continuous-subarray-sum/description/
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0:1}
        current_sum = 0
        total_count = 0

        for i, ele in enumerate(nums):
            current_sum += ele

            needed = current_sum - k
            if needed in prefix_map:
                total_count += prefix_map[needed]


            prefix_map[current_sum] = prefix_map.get(current_sum,0) + 1
        return total_count
