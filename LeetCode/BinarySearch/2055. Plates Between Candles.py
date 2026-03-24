'''
https://leetcode.com/problems/plates-between-candles/description/
'''
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        result = []
        for i in range(len(s)):
            if s[i] == "|":
                candles.append(i)

        
        for qleft,qright in queries:
            left_pos = -1
            right_pos = -1
            
            #find left_pos
            left = 0
            right = len(candles) - 1

            while left <= right:
                mid = (left + right) // 2
                if candles[mid] >= qleft:
                    right = mid - 1
                    left_pos = mid
                else:
                    left = mid + 1
            
            left = 0
            right = len(candles) - 1

            while left <= right:
                mid = (left + right) // 2
                if candles[mid] <= qright:
                    left = mid + 1
                    right_pos = mid
                else:
                    right = mid - 1


            if (left_pos != -1 and right_pos != -1) and (right_pos > left_pos):
                result.append((candles[right_pos] - candles[left_pos]) - (right_pos - left_pos))
            else:
                result.append(0)
        return result

            
