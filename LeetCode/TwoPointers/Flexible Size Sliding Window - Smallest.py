'''

nums = [2, 3, 1, 2, 4, 3], target = 7
Output : [4, 3]
'''

def subarray_sum_smallest(nums: list[int], target: int) -> int:
    # 1. Initialize trackers
    window_sum = 0
    window_len = float('inf')
    left = 0
    
    # 2. Iterate with the right pointer
    for right in range(len(nums)):
        window_sum += nums[right]
        
        # 3. Shrink WHILE the condition (sum >= target) is met
        while window_sum >= target:
            # Record the minimum length found so far
            window_len = min(window_len, (right - left + 1))
            
            # Try to shrink from the left
            window_sum -= nums[left]
            left += 1
            
    # 4. Return the result (handle case where no subarray was found)
    return window_len if window_len != float('inf') else 0

if __name__ == "__main__":
    # Example Input: 2 3 1 2 4 3
    # Target: 7
    nums = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_smallest(nums, target) # Updated name here
    print(res)
