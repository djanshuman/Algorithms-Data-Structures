'''
https://leetcode.com/problems/reverse-vowels-of-a-string/description/
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        l , r = 0, len(s) - 1
        res = list(s)
        vowels = "aeiouAEIOU"
    
        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                res[l] , res[r] = res[r] , res[l]
                l += 1
                r -= 1

        return "".join(res)


        
