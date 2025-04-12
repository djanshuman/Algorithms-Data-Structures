"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""


class Solution:
    def twoSum(self, numbers, target: int):
        l = 0
        r = len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l + 1, r + 1]


if __name__ == "__main__":
    numbers = [-1, 0]
    target = -1
    obj = Solution()
    print(obj.twoSum(numbers, target))
