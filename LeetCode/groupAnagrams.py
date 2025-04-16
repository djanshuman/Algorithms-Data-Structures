"""
https://leetcode.com/problems/group-anagrams/description/
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        final = {}

        for ele in strs:
            count = [0] * 26
            for i in ele:
                count[ord(i) - ord('a')] += 1
            res[tuple(count)].append(ele)
        return list(res.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    obj = Solution()
    print(obj.groupAnagrams(strs))
