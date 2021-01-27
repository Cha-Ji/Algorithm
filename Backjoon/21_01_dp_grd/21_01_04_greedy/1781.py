# Ex_1781 컵라면 [골드1]
import sys
import heapq

# 입력
N = int(input())
S = []  # 힙

# max heap
for _ in range(N):
    deadLine, cup = map(int, sys.stdin.readline().split())
    heapq.heappush(S, [-deadLine, -cup])

# 나중 데드라인부터 결정
day = -N
restCup = []
ans = 0
while day < 0:
    # 데드라인이 지나지 않은 문제를 힙에 올린다.
    if S and S[0][0] == day:
        thisDead, thisCup = heapq.heappop(S)
        heapq.heappush(restCup, thisCup)

        while S and thisDead == S[0][0]:
            thisCup = heapq.heappop(S)[1]
            heapq.heappush(restCup, thisCup)

    if restCup:
        ans -= heapq.heappop(restCup)
    day += 1
print(ans)
