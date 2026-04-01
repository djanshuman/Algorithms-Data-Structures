'''
https://leetcode.com/problems/longest-repeating-character-replacement/description/
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        myset = dict()
        max_len = - 1

        for r in range(len(s)):
            c = s[r]
            myset[c] = myset.get(c,0) + 1

            while (r - l + 1) - max(myset.values()) > k:
                myset[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
    
        return max_len

