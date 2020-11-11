N = int(input())
sum = [0] * N
floor = [sum] * N

for i in range(N):
    floor[i] = list(map(int, input().split(" ")))

for row in range(N):
    for col in range(row, 0, -1):
        sum[col] = max(sum[col-1], sum[col]) + floor[row][col]
    sum[0] += floor[row][0]
print(max(sum))

