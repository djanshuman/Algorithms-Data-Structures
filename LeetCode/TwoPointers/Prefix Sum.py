'''
Prefix Sum
Given an integer array arr and a target value, return a subarray whose sum equals the target. Return the answer as [start, end), where start is inclusive and end is exclusive.

Input: arr = [1, -20, -3, 30, 5, 4], target = 7

Output: [1, 4]

The subarray arr[1:4] = [-20, -3, 30] sums to 7.
'''
def subarray_sum(arr: list[int], target: int) -> list[int]:
    # WRITE YOUR BRILLIANT CODE HERE

    if len(arr) == 0:
        return [-1,-1]
        
    prefix_map = {0:-1}
    current_sum = 0

    for i , ele in enumerate(arr):
        current_sum += ele

        needed = current_sum - target
        if needed in prefix_map:
            index = prefix_map[needed] + 1
            return[index, i+1]

        if current_sum not in prefix_map:
            prefix_map[current_sum] = i
            
    return [-1,-1]
    
if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum(arr, target)
    print(" ".join(map(str, res)))
