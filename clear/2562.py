#Ex_2562
# base
Max=0
num=0
for i in range(9):
    N=int(input())
    if(Max<N):
        num=i+1
        Max=N
print(Max)
print(num)