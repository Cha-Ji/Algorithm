#Ex_1655
# priority Queue
# import heapq
# heap_Sort
import sys
import heapq
i =False
heap=[]
for _ in range(int(sys.stdin.readline())):
    i=not i
    heapq.heappush(heap,int(sys.stdin.readline()))
    heaped=[]
    for _ in range(len(heap)//2+1):
        heaped.append(heapq.heappop(heap))
    heap=heaped+heap
    print(heaped[-1] if (i or len(heaped)==1)
          else heaped[-2+ (heaped[-2] > heaped[-1])])
    print(heap)#tb
    print(heaped)#tb

