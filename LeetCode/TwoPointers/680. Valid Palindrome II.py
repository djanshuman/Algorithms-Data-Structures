'''
https://leetcode.com/problems/valid-palindrome-ii/description/
'''



class Solution:
    def validPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s) - 1

        #1. This block receives an incremented indices from the last palindrome failed check index.
        #2. On 1st mismatch occurs, this function is invoked which checks all futher string must be palindrome.
        def isPalin(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        #3. This checks the palindrome and calls for helper method when 1st mismatch is found to validate left over String.
        #4. If no mismatch found then proceed for usual palindrome check
        while l < r:
            if s[l] != s[r]:
                return isPalin(l+1 ,r) or isPalin(l ,r-1)
            l += 1
            r -= 1
        return True


''' 
Consider:What if you were allowed to delete up to k characters instead of just one? How would you adapt your current strategy?

'''
class Solution:
    def validPalindromeK(self, s: str, k: int) -> bool:

        def isPalin(l, r, remaining):
            while l < r:
                if s[l] != s[r]:
                    if remaining == 0:       # no deletions left → fail
                        return False
                    # try skipping left OR right, use 1 deletion
                    return isPalin(l+1, r, remaining-1) or isPalin(l, r-1, remaining-1)
                l += 1
                r -= 1
            return True

        return isPalin(0, len(s)-1, k)

