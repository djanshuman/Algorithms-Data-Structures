'''
https://leetcode.com/problems/valid-palindrome/description/
'''

class Solution:
    def isPalindrome(self, strs: str) -> bool:
        l=0
        r= len(strs)-1

        while (l < r):
            while l < r and not self.isAlpha(strs[l]):
                l+=1
            while l < r and not self.isAlpha(strs[r]):
                r-=1
            if strs[l].lower() !=strs[r].lower():
                return False
            l+=1
            r-=1
        return True

    def isAlpha(self,c):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')

        )
