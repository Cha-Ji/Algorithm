#Ex_1655
# priority Queue
# import heapq, tuple
import sys
import heapq
minH,maxH=[],[]
for _ in range(int(sys.stdin.readline())):
    m=int(sys.stdin.readline())
    if len(minH)==len(maxH):
        heapq.heappush(maxH,(-m,m))
        #heappush = minHeap
    else:
        heapq.heappush(minH,m)
    if (len(minH)and len(maxH))and maxH[0][1] > minH[0]:
        a=heapq.heappop(maxH)[1]
        b=heapq.heappop(minH)
        heapq.heappush(minH,a)
        heapq.heappush(maxH,(-b,b))
    print(maxH[0][1])



