# Ex_1655
# priority Queue
# import heapq, tuple
import sys
import heapq
input = sys.stdin.readline

minH, maxH = [10001], [10001]
plusMax = True
for i in range(int(input())):
    if plusMax:
        heapq.heappush(maxH, -int(input()))
    else:
        heapq.heappush(minH, int(input()))

    plusMax = not plusMax
    # 최대힙의 모든 원소는 최소힙의 모든 원소보다 작아야한다.
    # 서로의 최솟값을 주고받으며 유지시킨다.
    if -maxH[0] > minH[0]:
        a = -heapq.heappop(maxH)
        b = heapq.heappop(minH)
        heapq.heappush(minH, a)
        heapq.heappush(maxH, -b)

    print(-maxH[0])
