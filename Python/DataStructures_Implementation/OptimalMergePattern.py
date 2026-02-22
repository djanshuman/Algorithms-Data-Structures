import heapq

def optimal_merge_cost(list_size):

    heapq.heapify(list_size)
    total_cost = 0

    while(len(list_size)) > 1:

        first_list = heapq.heappop(list_size)
        sec_list = heapq.heappop(list_size)

        current_merge_cost = first_list + sec_list
        total_cost += current_merge_cost

        heapq.heappush(list_size,current_merge_cost)

    return total_cost

if __name__ == "__main__":
    # Example Usage:
    files = [20, 30, 10, 5, 30] # Example file sizes
    # Initially, the min-heap will order them as [5, 10, 20, 30, 30]
    min_cost = optimal_merge_cost(files)
    print(f"The minimum total merge cost is: {min_cost}") # Expected output for this example is 205
