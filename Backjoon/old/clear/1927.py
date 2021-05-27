#Ex_1927
# Min_Heap
# input x => pop(min)

import sys
def parent(index):
    return (index-1)//2
def child(index):
    return 2*index+1

def upHeap(heap):
    index=len(heap)-1
    while index > 0:
        if heap[index]<heap[parent(index)]:
            heap[index],heap[parent(index)]=heap[parent(index)],heap[index]
            index=parent(index)
        else:
            break
def downHeap(heap):
    index=0
    while child(index)<len(heap):
        if child(index)+1<len(heap) and heap[child(index)]>heap[child(index)+1]:
            smallest=child(index)+1
        else:smallest=child(index)
        if heap[index]>heap[smallest]:
            heap[index],heap[smallest]=heap[smallest],heap[index]
            index=smallest
        else:break

def delete_Heap(heap):
    if len(heap)==0:return 0
    elif len(heap)==1:return heap.pop()
    min_heap = heap[0]
    heap[0]=heap.pop()
    downHeap(heap)
    return min_heap

def insert_Heap(heap,item):
    heap.append(item)
    upHeap(heap)

heap=[]
for _ in range(int(sys.stdin.readline())):
    x=int(sys.stdin.readline())
    if x==0:
        print(delete_Heap(heap))
    else:
        insert_Heap(heap,x)


