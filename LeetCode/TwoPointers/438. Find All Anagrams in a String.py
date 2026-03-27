'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        # define ascii window for all a-z alphabets
        # initialize length and variables
        check_window = [0] * 26
        window = [0] * 26
        len_check = len(p)
        len_original = len(s)
        a = ord('a')
        res = []

        # one-time window initialization and mark first result if true
        for i in range(len_check):
            check_window[ord(p[i]) - a] += 1
            window[ord(s[i]) - a] += 1
        if check_window == window:
            res.append(0)

        # Now traverse sliding window , by adding one char right and remove 1 char left 

        for i in range(len_check,len_original):
            window[ord(s[i - len_check]) - a] -= 1
            window[ord(s[i]) - a] += 1

            if check_window == window:
                res.append( i - len_check +1)
        return res

