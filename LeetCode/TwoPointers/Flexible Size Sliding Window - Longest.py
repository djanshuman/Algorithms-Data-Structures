'''
Given an array of non-negative integers nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, the longest subarray that does not exceed 10 is [3, 1, 2, 4], so the output is 4.
'''

def subarray_sum_longest(nums: list[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    window_sum = 0
    window_len = 0
    left = 0
    for right in range(0,len(nums)):
        window_sum += nums[right]
        
        while window_sum > target:
            window_sum = window_sum - nums[left]
            left += 1
            
        window_len = max(window_len,(right-left+1))  
        
    return window_len
    
if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_longest(nums, target)
    print(res)
