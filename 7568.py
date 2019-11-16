#Ex_7568
# brute force
height = []
weight = []
T=int(input())
rank=[1]*T
for _ in range(T):
    N,M=map(int,input().split())
    weight.append(N)
    height.append(M)

for i in range(T):
    for j in range(T):
        if weight[i]<weight[j] and height[i]<height[j]:
            rank[i]+=1
for i in range(T):
    print(rank[i],end=" ")