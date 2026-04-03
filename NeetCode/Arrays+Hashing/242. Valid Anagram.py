'''
https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
          return False

        countS,countT= {},{}

        for i in range(len(s)):
            countS[s[i]]= 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i], 0)


        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
