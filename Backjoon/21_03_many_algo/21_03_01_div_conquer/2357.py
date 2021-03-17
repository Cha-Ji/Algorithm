# Ex_2357 최솟값과 최댓값 [골1]
import math
import sys
input = sys.stdin.readline
INF = sys.maxsize

# 일정 구간의 최소, 최댓값을 저장하는 트리


def init(node, s, e):
    if s == e:
        minT[node] = inputList[s]
        maxT[node] = inputList[s]

    else:
        lMin, lMax = init(node*2, s, (s+e) // 2)
        rMin, rMax = init(node*2 + 1, (s+e) // 2 + 1, e)

        minT[node] = min(lMin, rMin)
        maxT[node] = max(lMax, rMax)
    return minT[node], maxT[node]

# 트리에서 최소, 최댓값을 탐색


def search(node, s, e, l, r):
    if l > e or r < s:
        return INF, 0

    if l <= s and e <= r:
        return minT[node], maxT[node]

    lMin, lMax = search(node * 2, s, (s+e) // 2, l, r)
    rMin, rMax = search(node * 2 + 1, (s+e) // 2 + 1, e, l, r)

    return min(lMin, rMin), max(lMax, rMax)


N, M = map(int, input().split())
inputList = [int(input())for _ in range(N)]
minT = [INF] * pow(2, 18)
maxT = [0] * pow(2, 18)
init(1, 0, N - 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(*search(1, 0, N-1, a-1, b-1))
