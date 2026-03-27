'''
Fixed Size Sliding Window

Given an array (list) nums consisted of only non-negative integers, find the largest sum among all subarrays of length k in nums.

For example, if the input is nums = [1, 2, 3, 7, 4, 1], k = 3, then the output would be 14 as the largest length 3 subarray sum is given by [3, 7, 4] which sums to 14.


'''

def subarray_sum_fixed(nums: list[int], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    largest = window_sum
    for right in range(k,len(nums)):
        left = right - k
        window_sum -= nums[left]
        window_sum += nums[right]
        largest = max(largest,window_sum)
    
    return largest

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = subarray_sum_fixed(nums, k)
    print(res)
