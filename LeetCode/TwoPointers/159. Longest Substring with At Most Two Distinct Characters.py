'''
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
'''
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        res = 0
        count = dict()

        for r in range(len(s)):
            c = s[r]
            count[c] = count.get(c,0) + 1

            while len(count) > 2:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l+= 1
            res = max(res, r - l +1)
        return res




            
            


        
