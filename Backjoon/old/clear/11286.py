#Ex_11286
#Heap
import sys
def insert_Node(abs_heap,input_num):
    abs_heap.append(input_num)
    i=len(abs_heap)-1
    while i>0:
        if absMin(abs_heap,i,(i-1)//2):
            abs_heap[i],abs_heap[(i-1)//2] = \
                abs_heap[(i-1)//2],abs_heap[i]
            i=(i-1)//2
        else:break
def absMin(heap,i,family):
    if abs(heap[i])<abs(heap[family]) or \
            (heap[i]<0 and heap[family]+heap[i]==0):
        return True
    else:return False

def delete_Node(abs_heap):
    if len(abs_heap)==0:
        return 0
    elif len(abs_heap)==1:
        return abs_heap.pop()
    else:
        min_heap=abs_heap[0]
        abs_heap[0]=abs_heap.pop()
        i=0
        #down heap
        while 2*i+1 < len(abs_heap):
            smallest=2*i+1
            if 2*i+2 < len(abs_heap):
                if absMin(abs_heap,2*i+2,2*i+1):
                    smallest=2*i+2
            if absMin(abs_heap,smallest,i):
                abs_heap[i],abs_heap[smallest]= \
                    abs_heap[smallest],abs_heap[i]
            else:break
            i=smallest
        return min_heap

abs_heap=[]
for _ in range(int(sys.stdin.readline())):
    input_num=int(sys.stdin.readline())
    if input_num==0:
        print(delete_Node(abs_heap))
    else:
        insert_Node(abs_heap,input_num)
