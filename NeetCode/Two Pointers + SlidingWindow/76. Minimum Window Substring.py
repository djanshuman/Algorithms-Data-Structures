'''
https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150
https://leetcode.com/problems/minimum-window-substring/submissions/1965628832/
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t

        have = dict()
        need = dict()

        for c in t:
            need[c] = need.get(c,0) + 1

        found = 0
        satisfied = len(need)
        best_window = [-1, -1]
        best_len = float("inf")
        left = 0

        for right in range(len(s)):
            
            #1. Add element to have and expand right
            ele = s[right]
            have[ele] = have.get(ele,0) + 1

            if ele in need and have[ele] == need[ele]:
                found += 1

            #2. Shrinking window and take left off from left
            while found == satisfied:
                curr_len = right - left + 1
                curr_window = [left,right + 1]

                if curr_len < best_len:
                    best_len = curr_len
                    best_window = curr_window

                left_ele = s[left]
                have[left_ele] -= 1
                if left_ele in need and have[left_ele] < need[left_ele]:
                    found -= 1
                left += 1

        return s[best_window[0] : best_window[1]] if best_window[0] != -1 else ""


 
