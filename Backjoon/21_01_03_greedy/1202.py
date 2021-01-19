#Ex_1202 보석 도둑 [골드2]
import sys
import heapq
# 보석 수, 가방 수
N, K = map(int, sys.stdin.readline().split())

# 무게 & 가격
gemHeap = []
for _ in range(N):
    weight, cost = list(map(int, sys.stdin.readline().split()))
    # 앞 원소(가격)을 기준으로 힙에 추가된다.
    heapq.heappush(gemHeap, [weight, cost])

# 가방
bagHeap = []
for _ in range(K):
    C = int(sys.stdin.readline())
    heapq.heappush(bagHeap, C)

# 가방을 pop, 담을 수 있는 무게를 담는다.
ans = 0
miniGem = []
for _ in range(K):
    bag = heapq.heappop(bagHeap)
    
    # bag보다 작은 모든 보석
    while gemHeap and bag >= gemHeap[0][0]:
        weight, cost = heapq.heappop(gemHeap)
        heapq.heappush(miniGem, -cost) #최대힙 만들기

    # 보석이 있으면 가방에 추가
    if miniGem:
        # 최대힙을 만들기 위해 -cost를 힙에 넣었기 때문에
        # -=을 해준다.
        ans -= heapq.heappop(miniGem)

    # 보석이 더 적을 때
    elif not gemHeap:
        break
print(ans)
