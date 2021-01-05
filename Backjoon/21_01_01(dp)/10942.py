# Ex_10942 펠린드롬
# 시간제한이 엄격한 문제이다.

import sys
#입력
N = int(sys.stdin.readline()) # 수열의 크기
list_N = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

dp = [[False for _ in range(N+1)]for _ in range(N+1)]

# 회문 양 옆에 같은 숫자가 붙으면 회문이다.
# 회문의 길이가 0, 1일 때 true라고 가정한다.
dp[0][0] = True
for i in range(1, N+1):
    #회문의 길이가 1
    dp[i][i] = True 
    #회문의 길이가 0 
    dp[i][i-1] = True

# group = 회문의 길이
for group in range(1, N+1):
    for start in range(1, N-group+1):
        dp[start][start+group] = (
            dp[start+1][start+group-1]             #이전 dp가 회문
            and 
            list_N[start-1] == list_N[start+group-1] #양 옆에 추가된 숫자가 같음
        )

for _ in range(M):
    S,E = map(int, sys.stdin.readline().split())
    print(dp[S][E])


