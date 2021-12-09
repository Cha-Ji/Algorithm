# Ex_1238 파티: [골3]
import heapq


def dijkstra(goOrCome):
    stoe = [float('inf')] * (N + 1)
    stoe[X] = 0

    mid = [[0, X]]
    while mid:
        # start to mid + mid to end < start to end ?
        stom, midNode = heapq.heappop(mid)  # weight, node
        for mtoe, endNode in graph[goOrCome][midNode]:
            # start to end > start to mid + mid to end
            if stoe[endNode] > stom + mtoe:
                stoe[endNode] = stom + mtoe
                heapq.heappush(mid, [stoe[endNode], endNode])

    return stoe


N, M, X = map(int, input().split())
graph = [[[] * (N + 1) for _ in range(N + 1)] for _ in range(2)]


for _ in range(M):
    s, e, w = map(int, input().split())
    graph[0][s].append([w, e])
    graph[1][e].append([w, s])

print(max(dijkstra(0)[i] + dijkstra(1)[i] for i in range(1, N + 1)))
