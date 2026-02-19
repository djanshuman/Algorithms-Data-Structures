import heapq


# Returns total weight of the Minimum Spanning Tree
def spanningTree(V, adj):
    # Min-heap storing (weight, vertex)
    pq = []
    visited = [False] * V
    res = 0

    # Start from node 0
    heapq.heappush(pq, (0, 0))

    while pq:

        wt, u = heapq.heappop(pq)

        if visited[u]:
            continue

        res += wt
        visited[u] = True
                #[[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]], [], []]
        # Push adjacent edges
        for v in adj[u]:
            if not visited[v[0]]:
                heapq.heappush(pq, (v[1], v[0]))

    return res


if __name__ == '__main__':
    V = 3
    adj = [[] for _ in range(V)]

    adj[0].append([1, 5])
    adj[1].append([0, 5])

    adj[1].append([2, 3])
    adj[2].append([1, 3])

    adj[0].append([2, 1])
    adj[2].append([0, 1])

    print(spanningTree(V, adj))
