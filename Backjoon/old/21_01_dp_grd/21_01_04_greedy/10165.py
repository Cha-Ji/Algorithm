# Ex_10165 버스 노선 [플5]
import sys

N = int(input())
M = int(input())

rail = [0] * M
recursionEnd = 0
for num in range(M):
    start, end = map(int, sys.stdin.readline().split())

    if start > end:
        recursionEnd = max(recursionEnd, end)
        end += N
    rail[num] = [start, end, num + 1]

# 출발이 빠른 순으로 검사
rail.sort(key=lambda x: (x[0], -x[1]))

# 도착이 이른 노선은 배제
end = recursionEnd
ans = []
for s, e, num in rail:
    if end < e:
        end = e
        ans.append(num)
ans.sort()

for i in ans:
    print(i, end=" ")
print()
