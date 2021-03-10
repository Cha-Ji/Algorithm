# Ex_2042 구간 합 구하기 [골1]
import sys
input = sys.stdin.readline


def init(node, s, e):
    if s == e:
        tree[node] = num[s]
    else:
        tree[node] = init(node * 2, s, (s + e) // 2) + \
            init(node * 2 + 1, (s + e) // 2 + 1, e)
    return tree[node]


def subset(node, b, c, l, r):
    if b <= l and r <= c:
        return tree[node]
    elif b > r or c < l:
        return 0
    else:
        return subset(node * 2, b, c, l, (l+r) // 2) + subset(node * 2 + 1, b, c, (l+r)//2 + 1, r)


def change(node, b, c, l, r):
    if l <= b <= r:
        tree[node] += c
        if l != r:
            change(node * 2, b, c, l, (l + r) // 2)
            change(node * 2 + 1, b, c, (l + r) // 2 + 1, r)


N, M, K = map(int, input().split())

num = [int(input()) for _ in range(N)]

tree = [0] * pow(2, 21)  # 2^(log N + 1)
init(1, 0, N-1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        node = subset(1, b-1, b-1, 0, N - 1)
    change(1, b-1, c - node, 0, N -
           1) if a == 1 else print(subset(1, b-1, c-1, 0, N-1))
