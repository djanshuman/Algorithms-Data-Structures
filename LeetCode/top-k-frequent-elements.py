"""

https://leetcode.com/problems/top-k-frequent-elements/description/
"""

class Solution:
    def topKFrequent(self, nums, k: int):
        ele_map = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            ele_map[i] = 1 + ele_map.get(i, 0)

        for key, v in ele_map.items():
            freq[v].append(key)

        res = []
        for ele in range(len(freq) - 1, 0, -1):
            for i in freq[ele]:
                if len(res) != k:
                    res.append(i)

        return res


if __name__ == "__main__":
    nums = [99, 99, 99, 1, 1, 1, 2, 2, 2, 500, 500, 500, 500, 3, 3, 3, 3, 3, 100]
    k = 3
    obj = Solution()
    print(obj.topKFrequent(nums, k))
