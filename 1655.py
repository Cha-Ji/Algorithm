#Ex_1655
# priority Queue
# heap_Sort
def even_Heap(heap):
    pre=(len(heap)-1)//2
    if len(heap)==1:
        return heap[pre]
    if heap[pre]>heap[pre+1]:
        return heap[pre+1]
    else:return heap[pre]

def insert_Heap(heap,item):
    heap.append(item)
    i=len(heap)-1
    while i>0:
        parent=(i-1)//2
        if heap[i]>heap[parent]:
            heap[i],heap[parent] = \
            heap[parent],heap[i]
            i=parent
        else:break
    return heap_Sort(heap)

def heap_Sort(heap):
    heaped=[]
    i=len(heap)
    for _ in range(i):
        if len(heap)==1:
            heaped.append(heap.pop())
        else:
            heaped.append(heap[0])
            heap[0]=heap.pop()
            heap=down_Heap(heap)
    return heaped

def down_Heap(heap):
    i=0
    while 2*i+1<len(heap):
        child=2*i+1
        if 2*i+2<len(heap):
            if heap[2*i+1]<heap[2*i+2]:
                child+=1

        if heap[i]<heap[child]:
            heap[i],heap[child]=\
            heap[child],heap[i]
            i=child
        else:break
    return heap

import sys

i =False
heap=[]

for _ in range(int(sys.stdin.readline())):
    i=not i
    input_num = int(sys.stdin.readline())
    heap=insert_Heap(heap,input_num)
    if i:
        sys.stdout.write(str(heap[(len(heap)//2)])+"\n")
    else:sys.stdout.write(str(even_Heap(heap))+"\n")
