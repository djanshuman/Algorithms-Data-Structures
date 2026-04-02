'''
https://leetcode.com/problems/sliding-window-maximum/description/
Pattern - Monotonically decreasing deque
'''

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # monotonically decreasing
        res = []

        for i , n in enumerate(nums):
            # 1. Front eviction — remove indices outside window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2. Back eviction — remove weaker candidates
            while dq and nums[dq[-1]] < n:
                dq.pop()
            
            # 3. Append after restructuring
            dq.append(i)

            # 4. Record result once window is full
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
