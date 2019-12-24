#Ex_2108
# sort
# 통계
import sys
def meaning(arr,N):
    result=0
    for i in range(8001):
        result += (i-4000)*arr[i]
    return round(result/N)

def medianing(arr,N):
    M=N
    for i in range(8001):
        M-=arr[i]
        if(M<=N//2):
            mid=i
            return mid-4000
    return
def moding(arr,max):
    check=0
    index_=0
    for i in range(8001):
        if(check==2):
            break
        elif(arr[i]==max):
            index_=i
            check+=1
    return index_-4000

def ranging(arr):
    max=0
    min=0
    for i in range(8001):
        if(arr[i]>0):
            min=i
            break
    for i in range(8000,0,-1):
        if(arr[i]>0):
            max=i
            break
    return max-min

N=int(input())

arr=[0]*8001
max=0

for i in range(N):
    arr_index=int(sys.stdin.readline())
    arr[arr_index+4000]+=1
    if(max<arr[arr_index+4000]):
        max=arr[arr_index+4000]

print(meaning(arr,N))
print(medianing(arr,N))
print(moding(arr,max))
print(ranging(arr))
