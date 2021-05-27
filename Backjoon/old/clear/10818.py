#Ex_10818
# base
T=int(input())
N=list(map(int,input().split(" ")))
Max=N[0]
Min=N[0]
for i in range(T):
    if(Max<N[i]):
        Max=N[i]
    if(Min>N[i]):
        Min=N[i]
print(Min,Max)