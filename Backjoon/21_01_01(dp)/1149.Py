# Ex_ 1149 RGB 거리

#집의 수 2 ~ 1000
N = int(input())

#각 집을 색칠하는 R, B, G 비용
RBG_cost = [[0,0,0]] * (N+1)
for i in range(N):
    RBG_cost[i] = list(map(int, input().split()))

#보텀업 디피를 사용한다. 두 경우를 비교하여 최솟값을 유지시킨다.
d = [1001] * N
min_cost = 1001 * N

#마지막에 칠한 색을 기억하자.
end = 0

for j in range(3):

    d[0] = RBG_cost[0][j]
    end = j
    for i in range(1, N):

        end1 = (end + 1) % 3
        end2 = (end + 2) % 3

        cost1 = RBG_cost[i][end1] + d[i-1]
        cost2 = RBG_cost[i][end2] + d[i-1]

        if cost1 < cost2:
            end = end1
            d[i] = cost1

        else:
            end = end2
            d[i] = cost2

    print(d[N-1])
    min_cost = min(d[N-1], min_cost)
print(min_cost)