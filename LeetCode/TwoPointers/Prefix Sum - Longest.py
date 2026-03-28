'''
Prefix Sum + Longest subArray for finding target 

Same as prefix sum logic i.e; hashMap + Prefix Sum but instead of returning indices we check max Len and retain the indices 
''


def subarray_sum(arr: list[int], target: int) -> list[int]:
    # WRITE YOUR BRILLIANT CODE HERE

    if len(arr) == 0:
        return [-1,-1]
        
    prefix_map = {0:-1}
    current_sum = 0
    max_len = -1
    indices = [-1,-1]

    for i , ele in enumerate(arr):
        current_sum += ele

        needed = current_sum - target
        
        if needed in prefix_map:
            start_index = prefix_map[needed] + 1
            curr_len = i+1 - start_index

            if curr_len > max_len:
                max_len = curr_len
                indices = [start_index, i+1]

        if current_sum not in prefix_map:
            prefix_map[current_sum] = i
            
    return indices
    
if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum(arr, target)
    print(" ".join(map(str, res)))
