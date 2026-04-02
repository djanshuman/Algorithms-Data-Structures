'''
https://leetcode.com/problems/daily-temperatures/description/

Monitonically increasing stack pattern
'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i , n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                idx = stack.pop()
                res[idx] = i - idx

            stack.append(i)
        return res
