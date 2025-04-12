"""
https://leetcode.com/problems/container-with-most-water/description/
"""


class Solution:
    def maxArea(self, height) -> int:

        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


if __name__ == "__main__":
    height = [8, 7, 2, 1]
    obj = Solution()
    print(obj.maxArea(height))
