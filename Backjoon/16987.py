#Ex_16987 계란으로 계란치기 [실버2]
N = int(input()) #계란의 수
S = [] #내구도
W = [] #무게
#입력
for i in range(N):
    a, b = list(map(int, input().split()))
    S.append(a)
    W.append(b)

ans = [0]
# n번째 계란으로 깨기
def dfs(n):
    # 정지조건
    if n >= N:
        this_ans = 0
        # 깨진 계란 수
        for life in S:
            if life <= 0:
                this_ans += 1
        ans[0] = max(this_ans, ans[0])
        return
    # 깨진계란으로 때리는 경우
    if S[n] <= 0:
        dfs(n+1)
    
    else:
        for i in range(N):
            # 자해 금지
            if n == i: continue

            # 교환
            if S[i] > 0:
                S[n] -= W[i]
                S[i] -= W[n]

                dfs(n+1)

                # 복구
                S[n] += W[i]
                S[i] += W[n]

            #다른거 교환
            else:
                dfs(n+1)
dfs(0)
print(ans[0])
