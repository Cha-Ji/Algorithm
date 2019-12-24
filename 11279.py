#Ex_11279
# MAX_HEAP
#배열, 자연수 x 삽입
#pop heap[0]

import sys
def insert_Heap(heap,item):
    heap.append(item)
    i = len(heap)-1
    while i>0:
        if heap[(i-1)//2]>heap[i]:
            return
        else:
            heap[(i-1)//2],heap[i]=heap[i],heap[(i-1)//2]
            i=(i-1)//2

def delete_Heap(heap):
    if len(heap)==0:return 0
    elif len(heap)==1:return heap.pop()
    max_heap=heap[0]
    heap[0]=heap.pop()
    i=0

    while 2*i+1<=len(heap)-1:
        if 2*i+2<=len(heap)-1 and heap[2*i+1] < heap[2*i+2]:
            largest = 2*i+2
        else:
            largest = 2*i+1
        if heap[i]>heap[largest]:
            return max_heap
        else:
            heap[i],heap[largest]=heap[largest],heap[i]
            i=largest

    return max_heap

heap=[]
for _ in range(int(sys.stdin.readline())):
    #input_num = int(input())
    input_num = int(sys.stdin.readline())
    if input_num == 0:
        print(delete_Heap(heap))
    else:
        insert_Heap(heap,input_num)
