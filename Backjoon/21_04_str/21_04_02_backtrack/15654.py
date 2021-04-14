# Ex_15654 N과 M(5): [실3]
def dfs(depth):
    if depth == M:
        print(*ans)

    for i in range(N):
        if not v[i]:
            v[i] = True
            ans.append(A[i])
            dfs(depth + 1)
            ans.pop()
            v[i] = False


N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

v = [False] * (N + 1)
ans = []

dfs(0)
