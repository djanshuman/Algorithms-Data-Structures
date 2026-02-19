
import heapq, sys
def dijkstra(adj,src):

    V = len(adj)
    dist = [sys.maxsize] * V
    heaplst = []

    dist[src] = 0
    # initial distance and node insert in heap
    heapq.heappush(heaplst,(0,src))

    while heaplst:

        d, u  = heapq.heappop(heaplst)

        if d > dist[u]:
            continue

        # relaxation process
        for v , w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heaplst,(dist[v],v))
    return dist

if __name__ == "__main__":
    src = 0

    adj = [
        [(1, 4), (2, 8)],
        [(0, 4), (4, 6), (2, 3)],
        [(0, 8), (3, 2), (1, 3)],
        [(2, 2), (4, 10)],
        [(1, 6), (3, 10)]
    ]

    result = dijkstra(adj, src)
    print(result)
