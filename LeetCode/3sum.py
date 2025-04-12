"""
https://leetcode.com/problems/3sum/
"""


class Solution:
    def threeSum(self, nums):
        resList = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                resSum = a + nums[l] + nums[r]
                if resSum > 0:
                    r -= 1
                elif resSum < 0:
                    l += 1
                else:
                    resList.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return resList


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    obj = Solution()
    print(obj.threeSum(nums))
