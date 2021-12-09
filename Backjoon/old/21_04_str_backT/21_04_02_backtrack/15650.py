# Ex_15650 N과 M(2) [실3]
def dfs(depth):
    if depth == M:
        print(*ans[1:])

    elif depth < M:
        for i in range(N):
            if not v[i] and ans[-1] < A[i]:  # 오름차순만 인정
                v[i] = True
                ans.append(A[i])
                dfs(depth + 1)
                v[ans.pop() - 1] = False  # 이미 출력한 원소를 되추적하며 방문 취소


N, M = map(int, input().split())
A = [i + 1 for i in range(N)]
v = [False] * N
ans = [0]
dfs(0)
