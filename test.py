#Ex_1655
# priority Queue
# import heapq
# heap_Sort
def even_Heap(heap):
    pre=(len(heap)-1)//2
    if len(heap)==1:
        return heap[pre]
    if heap[pre]>heap[pre+1]:
        return heap[pre+1]
    else:return heap[pre]

def insert_Heap(heap,item):
    heapq.heappush(heap,item)
    heaped=[]
    i=len(heap)
    for _ in range(i):
        if len(heap)==1:
            heaped.append(heap.pop())
        else:
            heaped.append(heap[0])
            heapq.heappop(heap)
    return heaped

import sys
import heapq

i =False
heap=[]

for _ in range(int(sys.stdin.readline())):
    i=not i
    input_num = int(sys.stdin.readline())
    heap=insert_Heap(heap,input_num)
    if i:
        sys.stdout.write(str(heap[(len(heap)//2)])+"\n")
    else:sys.stdout.write(str(even_Heap(heap))+"\n")
