# Ex_2042 구간 합 구하기 [골1]
import sys
import math
input = sys.stdin.readline


def init(node, s, e):
    if s == e:
        tree[node] = num[s]
        return tree[node]

    return init(node * 2, s, (s + e) // 2) + init(node * 2 + 1, (s + e) // 2 + 1, e)


def subset(node, b, c, l, r):
    if l <= b and c <= r:
        return tree[node]
    elif r > b or c < l:
        return 0
    else:
        return subset(node * 2, b, c, l, (l+r) // 2) + subset(node * 2 + 1, b, c, (l+r)//2 + 1, r)


def change(node, b, c, l, r):
    if l == r:
        tree[node] += c - b
    elif l <= b <= r:
        tree[node] += c - b
        change(node * 2, b, c, l, (l + r) // 2)
        change(node * 2 + 1, b, c, (l + r) // 2 + 1, r)


N, M, K = map(int, input().split())

num = [int(input()) for _ in range(N)]

tree = [0] * pow(2, 21)  # 2^(log N + 1)
init(1, 0, N-1)
for _ in range(M + K):
    a, b, c = map(int, input().split())

    change(1, b, c, 0, N-1) if a == 1 else print(subset(1, b, c, 0, N-1))
