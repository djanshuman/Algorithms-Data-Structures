"""

https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums, target: int):
        my_map = {}
        # using hashMap approach
        for i, n in enumerate(nums):
            diff = target - n
            if diff in my_map:
                return [my_map[diff], i]
            my_map[n] = i


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    obj = Solution()
    print(obj.twoSum(nums, target))
