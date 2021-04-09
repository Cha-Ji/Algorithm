# Ex_15663 N과 M(9): [실2]
def dfs(depth):
    if depth == M:
        print(*ans)

    end = -1
    for i in range(N):
        if not v[i] and end != A[i]:
            v[i] = True
            ans.append(A[i])
            dfs(depth + 1)
            end = ans.pop()
            v[i] = False


N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

v = [False] * (N + 1)
ans = []
dfs(0)
