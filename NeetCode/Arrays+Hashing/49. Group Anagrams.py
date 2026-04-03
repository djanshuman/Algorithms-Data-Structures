'''
https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mylist = defaultdict(list)
        
        for i in strs:
            ele = [0] * 26
            for j in i:
                ele[ord(j) - ord('a')] += 1
            mylist[tuple(ele)].append(i)

        return list(mylist.values())


