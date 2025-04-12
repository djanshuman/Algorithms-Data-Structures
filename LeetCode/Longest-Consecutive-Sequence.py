"""

https://leetcode.com/problems/longest-consecutive-sequence/

"""


class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)  # create set from list
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


if __name__ == "__main__":
    elements = [100, 4, 200, 1, 3, 2]
    obj = Solution()
    print(obj.longestConsecutive(elements))
