# Ex_ 1149 RGB 거리

#집의 수 2 ~ 1000
N = int(input())

#각 집을 색칠하는 R, B, G 비용 입력
RBG_cost = [[0,0,0]] * (N+1)
for i in range(N):
    RBG_cost[i] = list(map(int, input().split()))

#보텀업 디피를 사용한다.
# 각 단계마다 마지막에 같은 색 끼리 칠한 경우를 비교해서 경우의 수를 줄인다.
# d[집][색]
d = [[0, 0, 0]] * N
d[0] = [RBG_cost[0][0], RBG_cost[0][1], RBG_cost[0][2]]

for i in range(1, N):
    d[i] = [
        min(d[i-1][1] + RBG_cost[i][0], d[i-1][2] + RBG_cost[i][0]),
        min(d[i-1][0] + RBG_cost[i][1], d[i-1][2] + RBG_cost[i][1]),
        min(d[i-1][0] + RBG_cost[i][2], d[i-1][1] + RBG_cost[i][2])
    ]

print(min(d[N-1]))

