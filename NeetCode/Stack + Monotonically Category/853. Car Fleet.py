'''
https://leetcode.com/problems/car-fleet/description/
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position,speed),key = lambda x : x[0],reverse = True)
        
        for position, speed in pairs:
            time = (target - position)/speed
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
