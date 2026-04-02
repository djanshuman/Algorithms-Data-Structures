'''
https://leetcode.com/problems/sliding-window-maximum/description/
'''

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # monotonically decreasing order 
        res = []

        for i , n in enumerate(nums):

            # 1. Check if current window is valid - dq[0] should always store indices within current window.
            # If the index at dq[0] is far behind current window then perform front eviction
            # window check is  i - k + 1 , if i = 2 , range = 0 ,1 ,2 , if i = 3 , range is 1,2,3 , so for i = 3 , dq[0] is 0 then evict. This is invalid window. 
            while dq and dq[0] < i -k +1:
                dq.popleft() 

            # 2. Check if rule is followed and previous element is monitonically decreasing else perform back eviction
            # Rule is Decreasing order maintain, so if previous element is less than then evict.
            while dq and nums[dq[-1]] < n:
                dq.pop()

            # 3. Append element since 1 and 2 check is complete and deque self ordered itself.
            dq.append(i)

            # 4. Record max of current window only if we are at last element of window

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
