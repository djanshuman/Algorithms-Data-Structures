'''
https://leetcode.com/problems/get-the-maximum-score/description/
'''

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        i = j = 0
        sum1 = sum2 = 0
        total = 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1

            elif nums2[j] < nums1[i]:
                sum2 += nums2[j]
                j += 1

            else:
                total += max(sum1, sum2) + nums1[i]
                sum1 = sum2 = 0
                i += 1
                j += 1

        while i < len(nums1):
            sum1 += nums1[i]
            i += 1
        while j < len(nums2):
            sum2 += nums2[j]
            j += 1

        total += max(sum1,sum2)
        return total % MOD
